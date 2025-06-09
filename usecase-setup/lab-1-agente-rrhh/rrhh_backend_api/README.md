# 🏗️ RRHH Backend API - Sistema de Recibos de Sueldo

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Tabla de Contenidos
- [🏗️ RRHH Backend API - Sistema de Recibos de Sueldo](#️-rrhh-backend-api---sistema-de-recibos-de-sueldo)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [📖 Descripción](#-descripción)
  - [🔧 Funcionalidades](#-funcionalidades)
  - [🏛️ Arquitectura del Código](#️-arquitectura-del-código)
  - [📁 Estructura del Proyecto](#-estructura-del-proyecto)
  - [🚀 Instalación y Configuración](#-instalación-y-configuración)
    - [Prerrequisitos](#prerrequisitos)
    - [Instalación Local](#instalación-local)
    - [Instalación con Docker](#instalación-con-docker)
  - [📋 Endpoints de la API](#-endpoints-de-la-api)
    - [GET /](#get-)
    - [GET /hr/recibo/imagen](#get-hrreciboImagen)
  - [🧪 Pruebas de la API](#-pruebas-de-la-api)
  - [📊 Monitoreo y Logs](#-monitoreo-y-logs)
  - [🔒 Seguridad](#-seguridad)
  - [🐳 Dockerización](#-dockerización)
  - [🔧 Desarrollo y Mantenimiento](#-desarrollo-y-mantenimiento)

## 📖 Descripción

El **RRHH Backend API** es un servicio REST construido con FastAPI que proporciona acceso a recibos de sueldo de empleados. Este backend está diseñado para ser consumido por agentes de IA especializados en recursos humanos, ofreciendo una interfaz simple y eficiente para la obtención de documentos de nómina en formato markdown.

Este sistema forma parte del ecosistema de automatización de RRHH y actúa como el backend tradicional que expone datos de nóminas a través de APIs REST estándar.

## 🔧 Funcionalidades

- **✅ Servicio de Estado**: Endpoint de health check para verificar disponibilidad
- **🧾 Obtención de Recibos**: Recuperación de imágenes de recibos de sueldo por nombre de empleado
- **📝 Formato Markdown**: Conversión automática de imágenes en formato markdown para fácil visualización
- **🌐 CORS Habilitado**: Soporte completo para Cross-Origin Resource Sharing
- **📊 Auto-documentación**: Documentación automática con Swagger UI y ReDoc
- **🔄 Respuestas JSON**: Formato estructurado y consistente de respuestas

## 🏛️ Arquitectura del Código

### Componentes Principales

```python
# Importaciones principales
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
```

### FastAPI Application

```python
app = FastAPI(title="RRHH Backend API", description="API para recursos humanos")
```

La aplicación utiliza FastAPI como framework principal, configurado con:
- **título descriptivo** para la documentación automática
- **descripción clara** del propósito del servicio

### Configuración CORS

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**Configuración permisiva** que permite:
- Todos los orígenes (`allow_origins=["*"]`)
- Credenciales en requests cross-origin
- Todos los métodos HTTP
- Todos los headers personalizados

> ⚠️ **Nota de Seguridad**: En producción, se recomienda restringir los orígenes permitidos

### Endpoint de Health Check

```python
@app.get("/")
async def root():
    return {"message": "RRHH Backend API está funcionando"}
```

### Endpoint Principal de Recibos

```python
@app.get("/hr/recibo/imagen")
async def imagen_markdown(nombre_empleado: str):
    # URL de imagen dummy para demostración
    URL_IMAGEN = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.rafap.com.uy%2Fmvdcms%2Fimgnoticias%2F202109%2F9691.png&f=1&nofb=1&ipt=5ad647da537e4656bbad02f4fc95c261e1fd96611bc77c3984344fa7bb304fbc"
    markdown_str = f"![Imagen recibo de sueldo de {nombre_empleado}]({URL_IMAGEN})"
    
    return {"markdown": markdown_str}
```

**Funcionamiento**:
1. Recibe el `nombre_empleado` como parámetro de query
2. Genera un string markdown con la imagen del recibo
3. Retorna un objeto JSON con el markdown generado

> 📝 **Nota**: Actualmente utiliza una imagen dummy. En producción debería conectarse a un sistema real de nóminas.

## 📁 Estructura del Proyecto

```
rrhh_backend_api/
├── app.py              # Aplicación principal FastAPI
├── Dockerfile          # Configuración de contenedor Docker
├── requirements.txt    # Dependencias Python
└── README.md          # Documentación (este archivo)
```

## 🚀 Instalación y Configuración

### Prerrequisitos

- **Python 3.12+**
- **pip** (gestor de paquetes Python)
- **Docker** (opcional, para contenedorización)

### Instalación Local

1. **Navegar al directorio del proyecto**:
```bash
cd usecase-setup/lab-1-agente-rrhh/rrhh_backend_api
```

2. **Crear entorno virtual** (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación**:
```bash
python app.py
```

5. **Verificar funcionamiento**:
   - API disponible en: `http://localhost:8080`
   - Documentación Swagger: `http://localhost:8080/docs`
   - Documentación ReDoc: `http://localhost:8080/redoc`

### Instalación con Docker

1. **Construir la imagen Docker**:
```bash
docker build -t rrhh-backend-api .
```

2. **Ejecutar el contenedor**:
```bash
docker run -d -p 8080:8080 --name rrhh-api rrhh-backend-api
```

3. **Verificar logs del contenedor**:
```bash
docker logs rrhh-api
```

## 📋 Endpoints de la API

### GET /

**Descripción**: Health check del servicio

**Parámetros**: Ninguno

**Respuesta**:
```json
{
  "message": "RRHH Backend API está funcionando"
}
```

**Código de estado**: `200 OK`

### GET /hr/recibo/imagen

**Descripción**: Obtiene la imagen del recibo de sueldo de un empleado en formato markdown

**Parámetros de Query**:
- `nombre_empleado` (string, requerido): Nombre completo del empleado

**Ejemplo de Request**:
```bash
curl "http://localhost:8080/hr/recibo/imagen?nombre_empleado=Juan%20Pérez"
```

**Respuesta exitosa**:
```json
{
  "markdown": "![Imagen recibo de sueldo de Juan Pérez](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.rafap.com.uy%2Fmvdcms%2Fimgnoticias%2F202109%2F9691.png&f=1&nofb=1&ipt=5ad647da537e4656bbad02f4fc95c261e1fd96611bc77c3984344fa7bb304fbc)"
}
```

**Código de estado**: `200 OK`

## 🧪 Pruebas de la API

### Usando curl

```bash
# Health check
curl http://localhost:8080/

# Obtener recibo de sueldo
curl "http://localhost:8080/hr/recibo/imagen?nombre_empleado=María%20García"
```

### Usando Python requests

```python
import requests

# Health check
response = requests.get("http://localhost:8080/")
print(response.json())

# Obtener recibo
response = requests.get(
    "http://localhost:8080/hr/recibo/imagen",
    params={"nombre_empleado": "María García"}
)
print(response.json())
```

### Usando Swagger UI

1. Abrir `http://localhost:8080/docs`
2. Expandir el endpoint deseado
3. Hacer clic en "Try it out"
4. Introducir parámetros
5. Ejecutar la prueba

## 📊 Monitoreo y Logs

### Logs de la Aplicación

La aplicación utiliza el sistema de logging por defecto de uvicorn:

```bash
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```

### Métricas Disponibles

- **Health Status**: Verificable en el endpoint `/`
- **Request Logs**: Uvicorn registra automáticamente todas las requests
- **Response Times**: Incluidos en los logs de uvicorn

## 🔒 Seguridad

### Configuración Actual

- **CORS**: Configurado de manera permisiva (todos los orígenes)
- **HTTPS**: No configurado (solo HTTP en puerto 8080)
- **Autenticación**: No implementada
- **Rate Limiting**: No implementado

### Recomendaciones para Producción

1. **Restringir CORS**:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://tudominio.com"],  # Solo dominios específicos
    allow_credentials=True,
    allow_methods=["GET"],  # Solo métodos necesarios
    allow_headers=["*"],
)
```

2. **Implementar HTTPS**:
```python
if __name__ == "__main__":
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8080,
        ssl_keyfile="path/to/key.pem",
        ssl_certfile="path/to/cert.pem"
    )
```

3. **Agregar autenticación**:
```python
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer

security = HTTPBearer()

@app.get("/hr/recibo/imagen")
async def imagen_markdown(
    nombre_empleado: str,
    token: str = Depends(security)
):
    # Validar token
    if not validate_token(token):
        raise HTTPException(status_code=401, detail="Token inválido")
    # ... resto del código
```

## 🐳 Dockerización

### Dockerfile Explicado

```dockerfile
FROM python:3.12-slim          # Base image ligera con Python 3.12
WORKDIR /app                   # Directorio de trabajo en el contenedor
COPY requirements.txt .        # Copia archivo de dependencias
RUN pip install --no-cache-dir -r requirements.txt  # Instala dependencias
COPY . .                       # Copia código fuente
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]  # Comando de inicio
```

### Comandos Docker Útiles

```bash
# Construir imagen
docker build -t rrhh-backend-api .

# Ejecutar contenedor
docker run -p 8080:8080 rrhh-backend-api

# Ejecutar en background
docker run -d -p 8080:8080 --name rrhh-api rrhh-backend-api

# Ver logs
docker logs rrhh-api

# Parar contenedor
docker stop rrhh-api

# Eliminar contenedor
docker rm rrhh-api
```

## 🔧 Desarrollo y Mantenimiento

### Agregar Nuevos Endpoints

1. **Definir función async**:
```python
@app.get("/nuevo-endpoint")
async def nuevo_endpoint(parametro: str):
    # Lógica del endpoint
    return {"resultado": "datos"}
```

2. **Agregar validación**:
```python
from pydantic import BaseModel

class RequestModel(BaseModel):
    campo: str
    valor: int

@app.post("/endpoint-validado")
async def endpoint_validado(data: RequestModel):
    return {"procesado": data.campo}
```

### Conectar con Sistema Real

Para conectar con un sistema real de nóminas, reemplazar la lógica dummy:

```python
import httpx  # Cliente HTTP async

@app.get("/hr/recibo/imagen")
async def imagen_markdown(nombre_empleado: str):
    # Conectar con sistema real
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://sistema-nominas.com/api/recibo/{nombre_empleado}"
        )
        imagen_url = response.json()["imagen_url"]
    
    markdown_str = f"![Imagen recibo de sueldo de {nombre_empleado}]({imagen_url})"
    return {"markdown": markdown_str}
```

### Dependencias

Las dependencias están definidas en `requirements.txt`:

```
fastapi          # Framework web moderno y rápido
uvicorn          # Servidor ASGI para FastAPI  
python-multipart # Soporte para form data y file uploads
```

---

> 📚 **Documentación relacionada**: 
> - [FastAPI Documentation](https://fastapi.tiangolo.com/)
> - [Uvicorn Documentation](https://www.uvicorn.org/)
> - [Docker Documentation](https://docs.docker.com/)
