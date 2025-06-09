from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="RRHH Backend API", description="API para recursos humanos")

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "RRHH Backend API está funcionando"}

@app.get("/hr/recibo/imagen")
async def imagen_markdown(nombre_empleado: str):
    
    # Este es un ejemplo de URL de imagen dummy. En un caso real, deberías reemplazarla con la lógica necesaria para conseguir la URL de la imagen del recibo de sueldo real de la persona que lo solicita.
    URL_IMAGEN = "https://raw.github.ibm.com/skol/agentic-ai-client-bootcamp/main/usecases/business-automation/assets/Business_Automation_Architecture.png?token=GHSAT0AAAAAAACRRDF2M3IMYVB47U3OKTEE2CO6JQA"
    markdown_str = f"![Imagen recibo de sueldo de {nombre_empleado}]({URL_IMAGEN})"
    
    return {"markdown": markdown_str}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)