from fastmcp import FastMCP
from typing import Annotated, Optional
from pydantic import Field
import uvicorn
from tools.gestion_rrhh import obtener_detalles_empleado, actualizar_direccion, actualizar_cargo, dias_licencia_gozada, pedir_licencia 

mcp = FastMCP("RRHHServer")

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

@mcp.tool
def rrhh_actualizar_direccion(
    nueva_direccion: Annotated[str, Field(
        description="Nueva dirección del empleado",
        min_length=5,
        max_length=200
    )],
    nombre_completo_empleado: Annotated[Optional[str], Field(
        description="Nombre completo del empleado"
    )] = None,
    numero_empleado: Annotated[Optional[str], Field(
        description="Número de empleado (ID)"
    )] = None
) -> str:
    """Actualiza la dirección de un empleado."""
    return actualizar_direccion(nombre_completo_empleado, numero_empleado, nueva_direccion)

@mcp.tool
def rrhh_actualizar_cargo(
    nuevo_cargo: Annotated[str, Field(
        description="Nuevo cargo/posición del empleado",
        min_length=2,
        max_length=100
    )],
    nombre_completo_empleado: Annotated[Optional[str], Field(
        description="Nombre completo del empleado"
    )] = None,
    numero_empleado: Annotated[Optional[str], Field(
        description="Número de empleado (ID)"
    )] = None
) -> str:
    """Actualiza el cargo de un empleado."""
    return actualizar_cargo(nombre_completo_empleado, numero_empleado, nuevo_cargo)

@mcp.tool
def rrhh_consultar_dias_licencia(
    nombre_completo_empleado: Annotated[Optional[str], Field(
        description="Nombre completo del empleado"
    )] = None,
    numero_empleado: Annotated[Optional[str], Field(
        description="Número de empleado (ID)"
    )] = None
) -> str:
    """Consulta los días de licencia ya gozados por un empleado."""
    return dias_licencia_gozada(nombre_completo_empleado, numero_empleado)

@mcp.tool
def rrhh_solicitar_licencia(
    fecha_inicio: Annotated[str, Field(
        description="Fecha de inicio de la licencia en formato dd/mm/yyyy",
        pattern=r"^\d{2}/\d{2}/\d{4}$"
    )],
    fecha_fin: Annotated[str, Field(
        description="Fecha de fin de la licencia en formato dd/mm/yyyy",
        pattern=r"^\d{2}/\d{2}/\d{4}$"
    )],
    nombre_completo_empleado: Annotated[Optional[str], Field(
        description="Nombre completo del empleado"
    )] = None,
    numero_empleado: Annotated[Optional[str], Field(
        description="Número de empleado (ID)"
    )] = None
) -> str:
    """Procesa una solicitud de licencia para un empleado."""
    return pedir_licencia(nombre_completo_empleado, numero_empleado, fecha_inicio, fecha_fin)

http_app = mcp.http_app()

if __name__ == "__main__":
    uvicorn.run(http_app, host="0.0.0.0", port=8080)
