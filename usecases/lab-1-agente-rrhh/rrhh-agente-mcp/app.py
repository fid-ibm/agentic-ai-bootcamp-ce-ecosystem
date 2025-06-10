#######################################
# Importamos las librerías necesarias #
####################################### 

import os
import json
import time
import uuid
import uvicorn

from dotenv import load_dotenv
from typing import Dict, List, Any
from fastapi import FastAPI, Header
from pydantic import BaseModel
from fastapi.responses import StreamingResponse

from langchain_core.tools import tool
from langchain_ibm import ChatWatsonx
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage
from langchain_mcp_adapters.client import MultiServerMCPClient


##########
# Set Up #
########## 

load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="LangGraph Agent Connect | Recursos Humanos MCP")

# Define message schema
class Message(BaseModel):
    role: str
    content: str
    name: str = None
    
class ChatRequest(BaseModel):
    model: str
    messages: List[Dict[str, Any]]
    stream: bool = False

############################
# Definimos nuestras tools #
############################ 

# Inicializamos el cliente MCP para conectarnos a los servicios de RRHH.
mcp_url = os.getenv("RRHH_BACKEND_MCP_URL", "http://localhost:8080") + "/mcp"
client = MultiServerMCPClient(
    {
        "gestion_rrhh": {
            "url": mcp_url,
            "transport": "streamable_http",
        }
    }
)

########################################
# Creamos nuestro Agente con LangGraph #
######################################## 

async def create_agent():
    # Initialize the LLM
    parameters = {
        "frequency_penalty": 0,
        "max_tokens": 2000,
        "presence_penalty": 0,
        "temperature": 0,
        "top_p": 1
    }
    
    llm = ChatWatsonx(
        model_id="meta-llama/llama-3-2-90b-vision-instruct",
        url=os.getenv("WATSONX_URL"),
        project_id=os.getenv("WATSONX_PROJECT_ID"),
        apikey=os.getenv("WATSONX_API_KEY"),
        params=parameters
    )
    
    # Definimos el prompt incluyendo las herramientas disponibles
    prompt = (
        "Tu objetivo es ayudar a los empleados a consultar y realizar operaciones relacionadas con recursos humanos, "
        "como consultar datos personales, editarlos, solicitar licencia, etc. "
        "Utiliza las herramientas disponibles para responder a las consultas de los empleados. "
        "Recuerda que debes utilizar las herramientas RRHH para obtener información específica. "
        "Asegúrate de que las respuestas sean claras y útiles para los empleados.\n\n"
        "Herramientas disponibles:\n"
        "- rrhh_obtener_detalles_empleado: Obtiene todos los detalles de un empleado por nombre completo o ID.\n"
        "- rrhh_actualizar_direccion: Actualiza la dirección de un empleado.\n"
        "- rrhh_actualizar_cargo: Actualiza el cargo de un empleado.\n"
        "- rrhh_consultar_dias_licencia: Consulta los días de licencia ya gozados por un empleado.\n"
        "- rrhh_solicitar_licencia: Procesa una solicitud de licencia para un empleado.\n"
    )
    
    tools = await client.get_tools()
    
    # print(f"Available tools: {tools}")
    
    return create_react_agent(llm, tools, prompt=prompt)

# Create the agent
agent_executor = None

async def initialize_agent():
    global agent_executor
    if agent_executor is None:
        agent_executor = await create_agent()
    return agent_executor

#######################################################################
# Definimos nuestros 2 endpoints estándar del protocolo Agent Connect #
####################################################################### 

# Agent discovery endpoint
@app.get("/v1/agents")
async def discover_agents():
    return {
        "agents": [
            {
                "name": "Agente de Recursos Humanos",
                "description": "Agente especializado en ayudar a los empleados y solucionar consultas de RRHH.",
                "provider": {
                    "organization": "IBM Agentic Bootcamp",
                    "url": "https:ibm.com"
                },
                "version": "1.0.0",
                "documentation_url": "https://docs.example.com/langgraph-agent",
                "capabilities": {
                    "streaming": True
                }
            }
        ]
    }

# Chat completion endpoint
@app.post("/v1/chat")
async def chat_completion(request: ChatRequest, x_thread_id: str = Header(None)):
    # Initialize agent if not already done
    await initialize_agent()
    
    thread_id = x_thread_id or str(uuid.uuid4())
    
    # Convert the messages to LangChain format
    messages = []
    for msg in request.messages:
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            messages.append(AIMessage(content=msg["content"]))
    
    # Handle streaming
    if request.stream:
        return StreamingResponse(
            stream_response(messages, thread_id),
            media_type="text/event-stream"
        )
    else:
        # Execute the agent
        result = await agent_executor.ainvoke({"messages": messages})
        final_message = result["messages"][-1]
        
        # Format the response
        response = {
            "id": f"chatcmpl-{uuid.uuid4()}",
            "object": "chat.completion",
            "created": int(time.time()),
            "model": request.model,
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": final_message.content
                    },
                    "finish_reason": "stop"
                }
            ],
            "usage": {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0
            }
        }
        
        return response

########################
# Funciones Auxiliares #
######################## 

# Stream response function
async def stream_response(messages, thread_id):
    # Initialize agent if not already done
    await initialize_agent()
    
    # First, send a thinking step
    thinking_step = {
        "id": f"step-{uuid.uuid4()}",
        "object": "thread.run.step.delta",
        "thread_id": thread_id,
        "model": "langgraph-agent",
        "created": int(time.time()),
        "choices": [
            {
                "delta": {
                    "role": "assistant",
                    "step_details": {
                        "type": "thinking",
                        "content": "Analyzing the request and formulating a response..."
                    }
                }
            }
        ]
    }
    
    yield f"event: thread.run.step.delta\n"
    yield f"data: {json.dumps(thinking_step)}\n\n"
    
    # Execute the agent with streaming
    config = {"configurable": {"thread_id": thread_id}}
    
    # Get the agent's response
    result = await agent_executor.ainvoke({"messages": messages})
    final_message = result["messages"][-1]
    
    # Stream the final message
    message_chunks = split_into_chunks(final_message.content)
    
    for i, chunk in enumerate(message_chunks):
        message_delta = {
            "id": f"msg-{uuid.uuid4()}",
            "object": "thread.message.delta",
            "thread_id": thread_id,
            "model": "langgraph-agent",
            "created": int(time.time()),
            "choices": [
                {
                    "delta": {
                        "role": "assistant",
                        "content": chunk
                    }
                }
            ]
        }
        
        yield f"event: thread.message.delta\n"
        yield f"data: {json.dumps(message_delta)}\n\n"

# Helper function to split text into chunks
def split_into_chunks(text, chunk_size=10):
    words = text.split()
    chunks = []
    current_chunk = []
    
    for word in words:
        current_chunk.append(word)
        if len(current_chunk) >= chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
    
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return chunks

################
# Función Main #
################ 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)