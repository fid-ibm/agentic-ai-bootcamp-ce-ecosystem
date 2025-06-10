# 📄 Agente de Recibos de Sueldo (API)

![Arquitectura API](../assets/rrhh-agente-api.jpg)

## Descripción

El **Agente de Recibos de Sueldo** es un agente de inteligencia artificial especializado en proporcionar acceso rápido y eficiente a los recibos de sueldo de los empleados. Este agente se conecta directamente con APIs tradicionales de RRHH para obtener y visualizar los recibos de sueldo en formato markdown, facilitando la consulta de información salarial de manera conversacional.

## ¿Qué hace este agente?

Este agente está diseñado específicamente para:

- **Obtención de recibos de sueldo**: Recupera imágenes de recibos de sueldo por nombre de empleado
- **Visualización en markdown**: Convierte las imágenes en formato markdown para fácil visualización
- **Interfaz conversacional**: Permite solicitud natural de recibos de sueldo
- **Integración con APIs**: Se conecta con sistemas legacy de nóminas y RRHH
- **Respuesta inmediata**: Proporciona acceso rápido a documentos de nómina

## Cómo funciona

### Arquitectura Técnica

El agente está construido utilizando las siguientes tecnologías:

- **Framework**: LangGraph para la orquestación de agentes
- **LLM**: IBM Watsonx.ai (meta-llama/llama-3-2-90b-vision-instruct)
- **Conectividad**: HTTP requests para APIs tradicionales
- **API**: FastAPI con soporte para streaming
- **Despliegue**: Docker containerizado

### Flujo de Operación

1. **Recepción de solicitud**: El usuario solicita un recibo de sueldo en lenguaje natural
2. **Extracción de nombre**: El LLM identifica el nombre del empleado en la consulta
3. **Llamada a API**: Se realiza una petición HTTP al backend de RRHH
4. **Obtención de imagen**: Se recupera la URL de la imagen del recibo de sueldo (dummy)
5. **Formateo markdown**: Se convierte la imagen en formato markdown
6. **Entrega de resultado**: Se proporciona el recibo formateado al usuario

### Herramientas Disponibles

- `get_imagen_recibo_de_sueldo_markdown`: Obtiene la imagen del recibo de sueldo de un empleado y la retorna en formato markdown

## Setup e Instalación

### Prerrequisitos

- Python 3.12+
- Docker (opcional)
- Acceso a IBM Watsonx.ai
- Backend API de RRHH funcionando

### Instalación Local

1. **Crear un entorno virtual**:

  - **En macOS/Linux**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
  - **En Windows**:
    ```cmd
    python -m venv venv
    venv\Scripts\activate
    ```

2. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

1. **Configurar variables de entorno**:
```bash
cp .env.example .env
# Editar .env con las credenciales correspondientes
```

1. **Ejecutar el agente**:
```bash
python3 app.py
```

### Instalación con Docker

1. **Construir la imagen**:
```bash
docker build -t rrhh-agente-api .
```

2. **Ejecutar el contenedor**:
```bash
docker run -p 8080:8080 --env-file .env rrhh-agente-api
```

## Obtención de Credenciales

### IBM Watsonx.ai

1. Acceder a [IBM Cloud](https://cloud.ibm.com)
2. Crear un proyecto en Watsonx.ai
3. Asociar un Watsonx.ai Runtime a ese proyecto en _Manage_
4. Obtener:
   - `WATSONX_PROJECT_ID`: ID del proyecto
   - `WATSONX_API_KEY`: Clave de API de IBM Cloud
   - `WATSONX_URL`: URL del servicio Watsonx

### Backend API

1. Asegurar que el backend API esté desplegado
2. Configurar:
   - `RRHH_BACKEND_API_URL`: URL del servidor API de RRHH

### Archivo .env

```env
WATSONX_PROJECT_ID="your_project_id"
WATSONX_API_KEY="your_api_key"
WATSONX_URL="https://your-watsonx-url"
RRHH_BACKEND_API_URL="http://localhost:8080"
```

## Ejemplos de Operaciones

### 1. Solicitar Recibo de Sueldo

**Entrada (JSON Schema)**:
```json
{
  "model": "watsonx",
  "messages": [
    {
      "role": "user",
      "content": "Necesito mi recibo de sueldo. Mi nombre es Juan Pablo Tejera"
    }
  ],
  "stream": false
}
```

**Salida esperada**:
Aquí está tu recibo de sueldo:\n\n![Imagen recibo de sueldo de Juan Pablo Tejera](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.rafap.com.uy%2Fmvdcms%2Fimgnoticias%2F202109%2F9691.png&f=1&nofb=1&ipt=5ad647da537e4656bbad02f4fc95c261e1fd96611bc77c3984344fa7bb304fbc)

### 2. Solicitud con Variación de Lenguaje

**Entrada (JSON Schema)**:
```json
{
  "model": "watsonx",
  "messages": [
    {
      "role": "user",
      "content": "¿Puedes mostrarme el recibo de sueldo de María García?"
    }
  ],
  "stream": false
}
```

**Salida esperada**:
```markdown
![Imagen recibo de sueldo de María García](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.rafap.com.uy%2Fmvdcms%2Fimgnoticias%2F202109%2F9691.png&f=1&nofb=1&ipt=5ad647da537e4656bbad02f4fc95c261e1fd96611bc77c3984344fa7bb304fbc)
```

### 3. Solicitud Formal

**Entrada (JSON Schema)**:
```json
{
  "model": "watsonx",
  "messages": [
    {
      "role": "user",
      "content": "Solicito el recibo de sueldo correspondiente a Faustino Carrera"
    }
  ],
  "stream": false
}
```

**Salida esperada**:
```markdown
![Imagen recibo de sueldo de Faustino Carrera](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.rafap.com.uy%2Fmvdcms%2Fimgnoticias%2F202109%2F9691.png&f=1&nofb=1&ipt=5ad647da537e4656bbad02f4fc95c261e1fd96611bc77c3984344fa7bb304fbc)
```

### 4. Solicitud con Modo Streaming

**Entrada (JSON Schema)**:
```json
{
  "model": "watsonx",
  "messages": [
    {
      "role": "user",
      "content": "Quiero ver mi recibo de sueldo - Araceli Garrido"
    }
  ],
  "stream": true
}
```

**Salida esperada (streaming)**:
```json
event: thread.run.step.delta
data: {"id": "step-afaa5492-e974-4833-b6be-cfc5c92fb266", "object": "thread.run.step.delta", "thread_id": "feba6c46-40c5-42eb-80d4-91c15c9cd57b", "model": "langgraph-agent", "created": 1749525380, "choices": [{"delta": {"role": "assistant", "step_details": {"type": "thinking", "content": "Analyzing the request and formulating a response..."}}}]}

event: thread.message.delta
data: {"id": "msg-710805a9-cc35-41ad-9ece-7e664261b9a9", "object": "thread.message.delta", "thread_id": "feba6c46-40c5-42eb-80d4-91c15c9cd57b", "model": "langgraph-agent", "created": 1749525388, "choices": [{"delta": {"role": "assistant", "content": "Aqu\u00ed est\u00e1 tu recibo de sueldo Araceli Garrido: ![Imagen recibo"}}]}

event: thread.message.delta
data: {"id": "msg-37072195-96e8-4d57-b977-20c57b9ad179", "object": "thread.message.delta", "thread_id": "feba6c46-40c5-42eb-80d4-91c15c9cd57b", "model": "langgraph-agent", "created": 1749525388, "choices": [{"delta": {"role": "assistant", "content": "de sueldo de Araceli Garrido](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.rafap.com.uy%2Fmvdcms%2Fimgnoticias%2F202109%2F9691.png&f=1&nofb=1&ipt=5ad647da537e4656bbad02f4fc95c261e1fd96611bc77c3984344fa7bb304fbc)"}}]}


```

## Endpoints de la API

### GET /v1/agents
Endpoint de descubrimiento de agentes compatible con Agent Connect Protocol.

**Respuesta**:
```json
{
  "agents": [
    {
      "name": "Agente de Recursos Humanos",
      "description": "Agente especializado en ayudar a los empleados con sus recibos de sueldo y consultas de RRHH.",
      "provider": {
        "organization": "IBM Agentic Bootcamp",
        "url": "https://ibm.com"
      },
      "version": "1.0.0",
      "capabilities": {
        "streaming": true
      }
    }
  ]
}
```

### POST /v1/chat
Endpoint principal para interacción con el agente. Soporta streaming y modo sincrónico.

**Headers**:
- `x-thread-id` (opcional): Identificador de hilo de conversación

**Request Body**:
```json
{
  "model": "string",
  "messages": [
    {
      "role": "user|assistant",
      "content": "string"
    }
  ],
  "stream": boolean
}
```

**Response (non-streaming)**:
```json
{
  "id": "chatcmpl-uuid",
  "object": "chat.completion",
  "created": 1676246400,
  "model": "watsonx",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "![Imagen recibo de sueldo de ...](...)"
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
```

## Integración con Backend API

### Endpoint del Backend

El agente se conecta con el siguiente endpoint del backend:

```
GET /hr/recibo/imagen?nombre_empleado={nombre}
```

**Respuesta esperada del backend**:
```json
{
  "markdown": "![Imagen recibo de sueldo de {nombre}]({url_imagen})"
}
```

### Configuración de la Herramienta

La herramienta `get_imagen_recibo_de_sueldo_markdown` realiza las siguientes operaciones:

1. Construye la URL del endpoint con el parámetro `nombre_empleado`
2. Realiza una petición GET al backend
3. Extrae el campo `markdown` de la respuesta JSON
4. Retorna el markdown formateado o un mensaje de error

## Limitaciones y Consideraciones

- **Dependencia del backend**: Requiere que la API backend esté disponible
- **Formato de imagen**: Las imágenes se muestran como markdown (enlaces)
- **Identificación por nombre**: Solo acepta nombre completo del empleado
- **Sin autenticación**: No verifica la identidad del solicitante
- **Imagen dummy**: En la implementación actual usa una imagen de ejemplo

## Casos de Uso Típicos

1. **Autoservicio de empleados**: Los empleados pueden obtener sus recibos sin contactar RRHH
2. **Verificación rápida**: Consulta inmediata de información salarial
3. **Integración con sistemas legacy**: Conecta sistemas antiguos con interfaces modernas
4. **Soporte remoto**: Facilita el acceso a documentos para empleados remotos

## Soporte y Mantenimiento

Para soporte técnico o reportar problemas:
- Verificar conectividad con el backend API
- Revisar logs de la aplicación para errores de conexión
- Validar credenciales de Watsonx.ai
- Confirmar que el endpoint `/hr/recibo/imagen` responde correctamente
- Revisar formato de respuesta del backend API