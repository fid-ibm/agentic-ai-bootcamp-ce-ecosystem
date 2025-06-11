#######################################
# Importamos las librerías necesarias #
####################################### 

import os
import json
import time
import uuid
import uvicorn
import requests

from dotenv import load_dotenv
from typing import Dict, List, Any
from fastapi import FastAPI, Header
from pydantic import BaseModel
from fastapi.responses import StreamingResponse

from langchain_core.tools import tool
from langchain_ibm import ChatWatsonx
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage

##########
# Set Up #
########## 

load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="LangGraph Agent Connect | Recursos Humanos API")

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

# Insertar aquí las herramientas que necesitemos para el agente

########################################
# Creamos nuestro Agente con LangGraph #
######################################## 

def create_agent():
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
    
    # Define un prompt para tu agente.
    prompt = (
    )
    
    # Agregamos las tools necesarias al agente
    tools = []
    
    return create_react_agent(llm, tools, prompt=prompt)

# Create the agent
agent_executor = create_agent()

#######################################################################
# Definimos nuestros 2 endpoints estándar del protocolo Agent Connect #
####################################################################### 

# Agent discovery endpoint
@app.get("/v1/agents")
async def discover_agents():
    return {
        "agents": [
            {
                "name": "LangGraph Tool Agent",
                "description": "A LangGraph agent with tool calling capabilities",
                "provider": {
                    "organization": "Your Organization",
                    "url": "https://your-organization.com"
                },
                "version": "1.0.0",
                "documentation_url": "https://docs.example.com/langgraph-tool-agent",
                "capabilities": {
                    "streaming": True
                }
            }
        ]
    }

# Chat completion endpoint
@app.post("/v1/chat")
async def chat_completion(request: ChatRequest, x_thread_id: str = Header(None)):
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
        result = agent_executor.invoke({"messages": messages})
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
    result = agent_executor.invoke({"messages": messages})
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