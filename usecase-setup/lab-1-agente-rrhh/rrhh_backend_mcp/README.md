# 🤖 RRHH Backend MCP - Sistema de Gestión de Recursos Humanos

## Tabla de Contenidos
- [🤖 RRHH Backend MCP - Sistema de Gestión de Recursos Humanos](#-rrhh-backend-mcp---sistema-de-gestión-de-recursos-humanos)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [📖 Descripción](#-descripción)
  - [🔧 Funcionalidades](#-funcionalidades)
  - [🏛️ Arquitectura del Código](#️-arquitectura-del-código)
    - [Servidor MCP Principal](#servidor-mcp-principal)
    - [Herramientas Disponibles](#herramientas-disponibles)
    - [Sistema de Gestión de Datos](#sistema-de-gestión-de-datos)
  - [📁 Estructura del Proyecto](#-estructura-del-proyecto)
  - [🚀 Instalación y Configuración](#-instalación-y-configuración)
    - [Prerrequisitos](#prerrequisitos)
    - [Instalación Local](#instalación-local)
    - [Instalación con Docker](#instalación-con-docker)
  - [🛠️ Herramientas MCP Disponibles](#️-herramientas-mcp-disponibles)
    - [rrhh\_obtener\_detalles\_empleado](#rrhh_obtener_detalles_empleado)
    - [rrhh\_actualizar\_direccion](#rrhh_actualizar_direccion)
    - [rrhh\_actualizar\_cargo](#rrhh_actualizar_cargo)
    - [rrhh\_consultar\_dias\_licencia](#rrhh_consultar_dias_licencia)
    - [rrhh\_solicitar\_licencia](#rrhh_solicitar_licencia)
  - [💾 Sistema de Datos](#-sistema-de-datos)
    - [Estructura del CSV](#estructura-del-csv)
    - [Empleados de Ejemplo](#empleados-de-ejemplo)
  - [🧪 Pruebas del Sistema](#-pruebas-del-sistema)
    - [Prueba de Consulta de Empleado](#prueba-de-consulta-de-empleado)
    - [Prueba de Actualización](#prueba-de-actualización)
    - [Prueba de Licencias](#prueba-de-licencias)
  - [📋 API de Gestión RRHH](#-api-de-gestión-rrhh)
    - [Funciones Principales](#funciones-principales)
      - [`_load_employees() -> List[Dict[str, str]]`](#_load_employees---listdictstr-str)
      - [`_save_employees(employees: List[Dict[str, str]]) -> None`](#_save_employeesemployees-listdictstr-str---none)
      - [`_find_employee(nombre_completo_empleado, numero_empleado) -> Optional[Dict[str, str]]`](#_find_employeenombre_completo_empleado-numero_empleado---optionaldictstr-str)
      - [`_calculate_days_between_dates(start_date: str, end_date: str) -> int`](#_calculate_days_between_datesstart_date-str-end_date-str---int)
    - [Validaciones Implementadas](#validaciones-implementadas)
  - [🔒 Seguridad y Validaciones](#-seguridad-y-validaciones)
    - [Validaciones de Entrada](#validaciones-de-entrada)
    - [Manejo de Errores](#manejo-de-errores)
    - [Límites del Sistema](#límites-del-sistema)
  - [🐳 Dockerización](#-dockerización)
    - [Dockerfile Explicado](#dockerfile-explicado)
    - [Comandos Docker Útiles](#comandos-docker-útiles)
  - [🔧 Desarrollo y Mantenimiento](#-desarrollo-y-mantenimiento)
    - [Agregar Nuevas Herramientas MCP](#agregar-nuevas-herramientas-mcp)
    - [Modificar Validaciones](#modificar-validaciones)
    - [Conectar con Base de Datos](#conectar-con-base-de-datos)
    - [Dependencias](#dependencias)
  - [📚 ¿Qué es Model Context Protocol (MCP)?](#-qué-es-model-context-protocol-mcp)
    - [Beneficios de MCP en este Sistema](#beneficios-de-mcp-en-este-sistema)
    - [Arquitectura MCP en este Sistema](#arquitectura-mcp-en-este-sistema)

## 📖 Descripción

El **RRHH Backend MCP** es un servidor basado en Model Context Protocol (MCP) que proporciona herramientas especializadas para la gestión integral de recursos humanos. Este sistema utiliza FastMCP para exponer funcionalidades de RRHH como herramientas que pueden ser utilizadas por agentes de IA de manera estándar y eficiente.

El servidor maneja un sistema completo de gestión de empleados con capacidades de consulta, actualización y validación de datos, incluyendo gestión de licencias con límites y validaciones empresariales.

## 🔧 Funcionalidades

- **Gestión de Empleados**: Consulta completa de información de empleados por nombre o ID
- **Actualización de Direcciones**: Modificación de direcciones de empleados con validación
- **Gestión de Cargos**: Actualización de posiciones y roles de empleados
- **Sistema de Licencias**: Consulta y solicitud de días de licencia con límites anuales
- **Validaciones Automáticas**: Control de límites de licencia y validación de fechas
- **Respuestas en Markdown**: Formateo automático de respuestas para mejor legibilidad
- **Persistencia de Datos**: Almacenamiento en CSV con operaciones CRUD
- **Manejo de Errores**: Respuestas descriptivas sin excepciones

## 🏛️ Arquitectura del Código

### Servidor MCP Principal

```python
from fastmcp import FastMCP
from typing import Annotated, Optional
from pydantic import Field
import uvicorn
from tools.gestion_rrhh import obtener_detalles_empleado, actualizar_direccion, actualizar_cargo, dias_licencia_gozada, pedir_licencia 

mcp = FastMCP("RRHHServer")
```

El servidor utiliza **FastMCP** como framework base para crear un servidor MCP que expone herramientas de RRHH.

### Herramientas Disponibles

Cada herramienta está decorada con `@mcp.tool` y utiliza **Pydantic** para validación de parámetros:

```python
@mcp.tool
def rrhh_obtener_detalles_empleado(
    nombre_completo_empleado: Annotated[Optional[str], Field(
        description="Nombre completo del empleado"
    )] = None,
    numero_empleado: Annotated[Optional[str], Field(
        description="Número de empleado (ID)"
    )] = None
) -> str:
    """Obtiene todos los detalles de un empleado por nombre completo o ID."""
    return obtener_detalles_empleado(nombre_completo_empleado, numero_empleado)
```

### Sistema de Gestión de Datos

El sistema utiliza funciones especializadas ubicadas en `tools/gestion_rrhh.py`:

- **Carga de datos**: `_load_employees()` - Carga empleados desde CSV
- **Guardado de datos**: `_save_employees()` - Persiste cambios en CSV
- **Búsqueda**: `_find_employee()` - Encuentra empleados por nombre o ID
- **Cálculos**: `_calculate_days_between_dates()` - Calcula días entre fechas

## 📁 Estructura del Proyecto

```
rrhh_backend_mcp/
├── app.py                 # Servidor MCP principal
├── Dockerfile            # Configuración Docker
├── requirements.txt      # Dependencias Python
├── README.md            # Documentación (este archivo)
└── tools/
    ├── __init__.py      # Paquete Python
    ├── gestion_rrhh.py  # Lógica de negocio RRHH
    └── base_empleados.csv # Base de datos de empleados
```

## 🚀 Instalación y Configuración

### Prerrequisitos

- **Python 3.12+**
- **pip** (gestor de paquetes Python)
- **Docker** (opcional, para contenedorización)

### Instalación Local

1. **Navegar al directorio del proyecto**:
```bash
cd usecase-setup/lab-1-agente-rrhh/rrhh_backend_mcp
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

4. **Ejecutar el servidor MCP**:
```bash
python app.py
```

5. **Verificar funcionamiento**:
   - Servidor MCP disponible en: `http://localhost:8080`
   - El servidor expondrá las herramientas MCP automáticamente

### Instalación con Docker

1. **Construir la imagen Docker**:
```bash
docker build -t rrhh-backend-mcp .
```

2. **Ejecutar el contenedor**:
```bash
docker run -d -p 8080:8080 --name rrhh-mcp rrhh-backend-mcp
```

3. **Verificar logs del contenedor**:
```bash
docker logs rrhh-mcp
```

## 🛠️ Herramientas MCP Disponibles

### rrhh_obtener_detalles_empleado

**Descripción**: Obtiene información completa de un empleado

**Parámetros**:
- `nombre_completo_empleado` (opcional): Nombre completo del empleado
- `numero_empleado` (opcional): ID numérico del empleado

**Ejemplo de uso**:
```python
# Por nombre
resultado = rrhh_obtener_detalles_empleado(nombre_completo_empleado="Faustino Carrera")

# Por ID
resultado = rrhh_obtener_detalles_empleado(numero_empleado="1")
```

**Respuesta**:
```markdown
## Detalles del Empleado

**Número de Empleado:** 1
**Nombre Completo:** Faustino Carrera
**Cargo:** QA Tester
**Dirección:** Callejón de Cesar Ponce 15, Castellón, 66943
**Días de Licencia Gozados:** 16
```

### rrhh_actualizar_direccion

**Descripción**: Actualiza la dirección de residencia de un empleado

**Parámetros**:
- `nueva_direccion` (requerido): Nueva dirección (5-200 caracteres)
- `nombre_completo_empleado` (opcional): Nombre completo del empleado
- `numero_empleado` (opcional): ID numérico del empleado

**Validaciones**:
- Dirección debe tener entre 5 y 200 caracteres
- Debe identificarse al empleado por nombre o ID

**Ejemplo de uso**:
```python
resultado = rrhh_actualizar_direccion(
    nueva_direccion="Calle Nueva 123, Madrid, 28001",
    nombre_completo_empleado="Faustino Carrera"
)
```

### rrhh_actualizar_cargo

**Descripción**: Modifica el cargo/posición de un empleado

**Parámetros**:
- `nuevo_cargo` (requerido): Nuevo cargo (2-100 caracteres)
- `nombre_completo_empleado` (opcional): Nombre completo del empleado
- `numero_empleado` (opcional): ID numérico del empleado

**Validaciones**:
- Cargo debe tener entre 2 y 100 caracteres
- Debe identificarse al empleado por nombre o ID

### rrhh_consultar_dias_licencia

**Descripción**: Consulta los días de licencia gozados y disponibles

**Parámetros**:
- `nombre_completo_empleado` (opcional): Nombre completo del empleado
- `numero_empleado` (opcional): ID numérico del empleado

**Respuesta**:
```markdown
## Días de Licencia Gozados

**Empleado:** Faustino Carrera
**Días de Licencia ya Gozados:** 16 días
**Días restantes disponibles:** 14 días
```

### rrhh_solicitar_licencia

**Descripción**: Procesa una solicitud de licencia con validaciones automáticas

**Parámetros**:
- `fecha_inicio` (requerido): Fecha de inicio en formato dd/mm/yyyy
- `fecha_fin` (requerido): Fecha de fin en formato dd/mm/yyyy
- `nombre_completo_empleado` (opcional): Nombre completo del empleado
- `numero_empleado` (opcional): ID numérico del empleado

**Validaciones**:
- Formato de fecha válido (dd/mm/yyyy)
- Límite máximo de 30 días de licencia anual
- Cálculo automático de días solicitados

**Ejemplo de solicitud aprobada**:
```markdown
## Solicitud de Licencia Aprobada

**Empleado:** Faustino Carrera
**Período de Licencia:** 15/12/2024 - 20/12/2024
**Días Solicitados:** 6 días
**Total Días Gozados:** 22 días
**Días Restantes:** 8 días

Su solicitud de licencia ha sido aprobada y registrada exitosamente.
```

**Ejemplo de solicitud denegada**:
```markdown
## Solicitud de Licencia Denegada

**Empleado:** Faustino Carrera
**Días ya gozados:** 25
**Días solicitados:** 10
**Total:** 35 días

**Error:** No se puede tomar más de 30 días de licencia por año.

**Opciones disponibles:**
- Contactar al corresponsal de recursos humanos
- Enviar un email a rrhh@ibm.com con el motivo de la solicitud especial

**Email sugerido:** rrhh@ibm.com
```

## 💾 Sistema de Datos

### Estructura del CSV

El archivo `tools/base_empleados.csv` contiene la información de los empleados:

```csv
Número de Empleado,Nombre Completo,Cargo,Dirección,Días de Licencia
1,Faustino Carrera,QA Tester,"Callejón de Cesar Ponce 15, Castellón, 66943",16
2,Araceli Garrido,Desarrollador Backend,"Ronda Apolonia Aranda 1, Valencia, 57792",13
...
```

### Empleados de Ejemplo

El sistema incluye 100+ empleados con diferentes roles:

- **Desarrolladores**: Frontend, Backend, Full Stack
- **QA Testers**: Especialistas en calidad
- **DevOps**: Ingenieros de infraestructura
- **Product Owners**: Gestión de producto
- **Arquitectos**: Arquitectos de software
- **Diseñadores**: UX/UI
- **Soporte**: Técnico y sistemas

## 🧪 Pruebas del Sistema

### Prueba de Consulta de Empleado

```python
# Ejecutar desde el directorio del proyecto
from tools.gestion_rrhh import obtener_detalles_empleado

# Probar por nombre
resultado = obtener_detalles_empleado("Faustino Carrera")
print(resultado)

# Probar por ID
resultado = obtener_detalles_empleado(numero_empleado="1")
print(resultado)
```

### Prueba de Actualización

```python
from tools.gestion_rrhh import actualizar_direccion

resultado = actualizar_direccion(
    "Faustino Carrera", 
    None, 
    "Nueva Dirección de Prueba 456"
)
print(resultado)
```

### Prueba de Licencias

```python
from tools.gestion_rrhh import pedir_licencia

# Solicitud que debería aprobarse
resultado = pedir_licencia(
    "Faustino Carrera", 
    None, 
    "01/12/2024", 
    "05/12/2024"
)
print(resultado)
```

## 📋 API de Gestión RRHH

### Funciones Principales

#### `_load_employees() -> List[Dict[str, str]]`
Carga todos los empleados del archivo CSV y retorna una lista de diccionarios.

#### `_save_employees(employees: List[Dict[str, str]]) -> None`
Guarda la lista de empleados actualizada en el archivo CSV.

#### `_find_employee(nombre_completo_empleado, numero_empleado) -> Optional[Dict[str, str]]`
Busca un empleado específico por nombre o ID. Realiza búsqueda case-insensitive para nombres.

#### `_calculate_days_between_dates(start_date: str, end_date: str) -> int`
Calcula el número de días entre dos fechas en formato dd/mm/yyyy, incluyendo ambas fechas.

### Validaciones Implementadas

1. **Validación de Empleado**: Verifica que el empleado existe antes de cualquier operación
2. **Validación de Fechas**: Formato correcto dd/mm/yyyy
3. **Límites de Licencia**: Máximo 30 días anuales
4. **Longitud de Campos**: Direcciones (5-200 chars), Cargos (2-100 chars)
5. **Manejo de Errores**: Respuestas descriptivas sin excepciones

## 🔒 Seguridad y Validaciones

### Validaciones de Entrada

```python
# Validación con Pydantic Field
nueva_direccion: Annotated[str, Field(
    description="Nueva dirección del empleado",
    min_length=5,
    max_length=200
)]

# Validación de patrón de fecha
fecha_inicio: Annotated[str, Field(
    description="Fecha de inicio de la licencia en formato dd/mm/yyyy",
    pattern=r"^\d{2}/\d{2}/\d{4}$"
)]
```

### Manejo de Errores

El sistema no utiliza excepciones, sino que retorna mensajes descriptivos:

```python
if not employee:
    identifier = nombre_completo_empleado or numero_empleado
    return f"Error: Empleado '{identifier}' no encontrado."
```

### Límites del Sistema

- **Licencia anual máxima**: 30 días
- **Longitud de dirección**: 5-200 caracteres
- **Longitud de cargo**: 2-100 caracteres
- **Formato de fecha**: dd/mm/yyyy obligatorio

## 🐳 Dockerización

### Dockerfile Explicado

```dockerfile
FROM python:3.12-slim          # Base image ligera
WORKDIR /app                   # Directorio de trabajo
COPY requirements.txt .        # Copia dependencias
RUN pip install --no-cache-dir -r requirements.txt  # Instala paquetes
COPY . .                       # Copia código fuente
CMD ["uvicorn", "app:http_app", "--host", "0.0.0.0", "--port", "8080"]  # Inicia servidor
```

### Comandos Docker Útiles

```bash
# Construir imagen
docker build -t rrhh-backend-mcp .

# Ejecutar contenedor con montaje de volumen para persistencia
docker run -p 8080:8080 -v $(pwd)/tools:/app/tools rrhh-backend-mcp

# Ejecutar en background
docker run -d -p 8080:8080 --name rrhh-mcp rrhh-backend-mcp

# Ver logs en tiempo real
docker logs -f rrhh-mcp

# Acceder al contenedor
docker exec -it rrhh-mcp /bin/bash
```

## 🔧 Desarrollo y Mantenimiento

### Agregar Nuevas Herramientas MCP

1. **Crear función en gestion_rrhh.py**:
```python
def nueva_funcionalidad_rrhh(parametro: str) -> str:
    """Nueva funcionalidad de RRHH."""
    # Implementar lógica
    return "Resultado en markdown"
```

2. **Agregar herramienta MCP en app.py**:
```python
@mcp.tool
def rrhh_nueva_funcionalidad(
    parametro: Annotated[str, Field(description="Descripción del parámetro")]
) -> str:
    """Descripción de la nueva herramienta."""
    return nueva_funcionalidad_rrhh(parametro)
```

### Modificar Validaciones

Para cambiar límites o agregar validaciones:

```python
# En gestion_rrhh.py
MAX_LICENCIA_ANUAL = 25  # Cambiar límite de días

# Agregar nueva validación
def validar_email(email: str) -> bool:
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
```

### Conectar con Base de Datos

Para reemplazar CSV con base de datos:

```python
import sqlite3
# o
import psycopg2  # PostgreSQL
# o 
from sqlalchemy import create_engine

def _load_employees():
    conn = sqlite3.connect('rrhh.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empleados")
    employees = cursor.fetchall()
    conn.close()
    return employees
```

### Dependencias

Las dependencias están en `requirements.txt`:

```
fastmcp              # Framework MCP para Python
uvicorn             # Servidor ASGI
pydantic            # Validación de datos
typing-extensions   # Extensiones de tipos para Python
```

## 📚 ¿Qué es Model Context Protocol (MCP)?

Model Context Protocol (MCP) es un protocolo abierto que estandariza cómo las aplicaciones proporcionan contexto a los modelos de lenguaje grandes (LLMs). MCP es como "un puerto USB-C para aplicaciones de IA" - al igual que USB-C proporciona una forma estandarizada de conectar dispositivos, MCP proporciona una forma estandarizada de conectar modelos de IA a diferentes fuentes de datos y herramientas.

### Beneficios de MCP en este Sistema

1. **Estandardización**: Las herramientas de RRHH están disponibles de manera uniforme para cualquier cliente MCP
2. **Interoperabilidad**: Funciona con diferentes modelos de IA y frameworks
3. **Escalabilidad**: Fácil agregar nuevas herramientas sin cambiar la interfaz
4. **Type Safety**: Validación automática de parámetros con Pydantic
5. **Documentación Automática**: Las herramientas se autodocumentan

### Arquitectura MCP en este Sistema

```
Cliente MCP (Agente IA) <-> Servidor MCP (este sistema) <-> Base de Datos CSV
```

El servidor MCP actúa como intermediario entre los agentes de IA y los datos de RRHH, proporcionando herramientas especializadas y validadas para operaciones de recursos humanos.

---

> 📚 **Documentación relacionada**: 
> - [FastMCP Documentation](https://github.com/jlowin/fastmcp)
> - [Model Context Protocol Specification](https://modelcontextprotocol.io/)
> - [Pydantic Documentation](https://docs.pydantic.dev/)
> - [Uvicorn Documentation](https://www.uvicorn.org/)