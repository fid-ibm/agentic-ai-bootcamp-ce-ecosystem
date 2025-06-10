import csv
from datetime import datetime
from typing import Optional, Dict, List

# Constantes del sistema
CSV_PATH = "tools/base_empleados.csv"
HEADERS = ["Número de Empleado", "Nombre Completo", "Cargo", "Dirección", "Días de Licencia"]
MAX_LICENCIA_ANUAL = 30


# Sin excepciones - retornamos strings con mensajes de error


def _load_employees() -> List[Dict[str, str]]:
    """
    Carga todos los empleados del archivo CSV.
    
    Returns:
        List[Dict[str, str]]: Lista de diccionarios con información de empleados
    """
    employees = []
    with open(CSV_PATH, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row)
    return employees


def _save_employees(employees: List[Dict[str, str]]) -> None:
    """
    Guarda la lista de empleados en el archivo CSV.
    
    Args:
        employees (List[Dict[str, str]]): Lista de empleados a guardar
    """
    with open(CSV_PATH, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(employees)


def _find_employee(nombre_completo_empleado: Optional[str] = None, numero_empleado: Optional[str] = None) -> Optional[Dict[str, str]]:
    """
    Busca un empleado por nombre completo o ID.
    
    Args:
        nombre_completo_empleado (Optional[str]): Nombre completo del empleado
        numero_empleado (Optional[str]): ID del empleado
        
    Returns:
        Optional[Dict[str, str]]: Diccionario con datos del empleado o None si no se encuentra
    """
    if not nombre_completo_empleado and not numero_empleado:
        return None
        
    employees = _load_employees()
    
    for employee in employees:
        if nombre_completo_empleado and employee["Nombre Completo"].strip().lower() == nombre_completo_empleado.strip().lower():
            return employee
        if numero_empleado and employee["Número de Empleado"].strip() == str(numero_empleado).strip():
            return employee
    return None


def _calculate_days_between_dates(start_date: str, end_date: str) -> int:
    """
    Calcula los días entre dos fechas en formato dd/mm/yyyy.
    
    Args:
        start_date (str): Fecha de inicio en formato dd/mm/yyyy
        end_date (str): Fecha de fin en formato dd/mm/yyyy
        
    Returns:
        int: Número de días entre las fechas (incluyendo ambas fechas), -1 si hay error
    """
    try:
        start = datetime.strptime(start_date, "%d/%m/%Y")
        end = datetime.strptime(end_date, "%d/%m/%Y")
        return abs((end - start).days) + 1  # +1 para incluir ambas fechas
    except ValueError:
        return -1


def obtener_detalles_empleado(nombre_completo_empleado: Optional[str] = None, numero_empleado: Optional[str] = None) -> str:
    """
    Obtiene todos los detalles de un empleado.
    
    Args:
        nombre_completo_empleado (Optional[str]): Nombre completo del empleado
        numero_empleado (Optional[str]): ID del empleado
        
    Returns:
        str: Información del empleado formateada en markdown o mensaje de error
    """
    employee = _find_employee(nombre_completo_empleado, numero_empleado)
    if not employee:
        identifier = nombre_completo_empleado or numero_empleado
        return f"Error: Empleado '{identifier}' no encontrado."
    
    return f"""## Detalles del Empleado

**Número de Empleado:** {employee['Número de Empleado']}
**Nombre Completo:** {employee['Nombre Completo']}
**Cargo:** {employee['Cargo']}
**Dirección:** {employee['Dirección']}
**Días de Licencia Gozados:** {employee['Días de Licencia']}"""


def actualizar_direccion(nombre_completo_empleado: Optional[str] = None, numero_empleado: Optional[str] = None, nueva_direccion: str = "") -> str:
    """
    Actualiza la dirección de un empleado.
    
    Args:
        nombre_completo_empleado (Optional[str]): Nombre completo del empleado
        numero_empleado (Optional[str]): ID del empleado
        nueva_direccion (str): Nueva dirección del empleado
        
    Returns:
        str: Confirmación del cambio en markdown o mensaje de error
    """
    employees = _load_employees()
    employee_found = False
    
    for employee in employees:
        if ((nombre_completo_empleado and employee["Nombre Completo"].strip().lower() == nombre_completo_empleado.strip().lower()) or
            (numero_empleado and employee["Número de Empleado"].strip() == str(numero_empleado).strip())):
            employee["Dirección"] = nueva_direccion.strip()
            employee_found = True
            break
    
    if not employee_found:
        identifier = nombre_completo_empleado or numero_empleado
        return f"Error: Empleado '{identifier}' no encontrado."
    
    _save_employees(employees)
    
    updated_employee = _find_employee(nombre_completo_empleado, numero_empleado)
    return f"""## Dirección Actualizada

**Empleado:** {updated_employee['Nombre Completo']}
**Nueva Dirección:** **{updated_employee['Dirección']}**

La dirección ha sido actualizada exitosamente."""


def actualizar_cargo(nombre_completo_empleado: Optional[str] = None, numero_empleado: Optional[str] = None, nuevo_cargo: str = "") -> str:
    """
    Actualiza el cargo de un empleado.
    
    Args:
        nombre_completo_empleado (Optional[str]): Nombre completo del empleado
        numero_empleado (Optional[str]): ID del empleado
        nuevo_cargo (str): Nuevo cargo del empleado
        
    Returns:
        str: Confirmación del cambio en markdown o mensaje de error
    """
    employees = _load_employees()
    employee_found = False
    
    for employee in employees:
        if ((nombre_completo_empleado and employee["Nombre Completo"].strip().lower() == nombre_completo_empleado.strip().lower()) or
            (numero_empleado and employee["Número de Empleado"].strip() == str(numero_empleado).strip())):
            employee["Cargo"] = nuevo_cargo.strip()
            employee_found = True
            break
    
    if not employee_found:
        identifier = nombre_completo_empleado or numero_empleado
        return f"Error: Empleado '{identifier}' no encontrado."
    
    _save_employees(employees)
    
    updated_employee = _find_employee(nombre_completo_empleado, numero_empleado)
    return f"""## Cargo Actualizado

**Empleado:** {updated_employee['Nombre Completo']}
**Nuevo Cargo:** **{updated_employee['Cargo']}**

El cargo ha sido actualizado exitosamente."""


def dias_licencia_gozada(nombre_completo_empleado: Optional[str] = None, numero_empleado: Optional[str] = None) -> str:
    """
    Obtiene los días de licencia ya gozados por un empleado.
    
    Args:
        nombre_completo_empleado (Optional[str]): Nombre completo del empleado
        numero_empleado (Optional[str]): ID del empleado
        
    Returns:
        str: Información de días de licencia en markdown o mensaje de error
    """
    employee = _find_employee(nombre_completo_empleado, numero_empleado)
    if not employee:
        identifier = nombre_completo_empleado or numero_empleado
        return f"Error: Empleado '{identifier}' no encontrado."
    
    dias_gozados = int(employee['Días de Licencia'])
    dias_restantes = MAX_LICENCIA_ANUAL - dias_gozados
    
    return f"""## Días de Licencia Gozados

**Empleado:** {employee['Nombre Completo']}
**Días de Licencia ya Gozados:** **{dias_gozados}** días
**Días restantes disponibles:** **{dias_restantes}** días"""


def pedir_licencia(nombre_completo_empleado: Optional[str] = None, numero_empleado: Optional[str] = None, fecha_inicio: str = "", fecha_fin: str = "") -> str:
    """
    Procesa una solicitud de licencia para un empleado.
    
    Args:
        nombre_completo_empleado (Optional[str]): Nombre completo del empleado
        numero_empleado (Optional[str]): ID del empleado
        fecha_inicio (str): Fecha de inicio de la licencia (dd/mm/yyyy)
        fecha_fin (str): Fecha de fin de la licencia (dd/mm/yyyy)
        
    Returns:
        str: Confirmación o error en markdown
    """
    employee = _find_employee(nombre_completo_empleado, numero_empleado)
    if not employee:
        identifier = nombre_completo_empleado or numero_empleado
        return f"Error: Empleado '{identifier}' no encontrado."
    
    # Calcular días solicitados
    dias_solicitados = _calculate_days_between_dates(fecha_inicio, fecha_fin)
    if dias_solicitados == -1:
        return "Error: Formato de fecha inválido. Use dd/mm/yyyy."
    
    dias_actuales = int(employee['Días de Licencia'])
    total_dias = dias_actuales + dias_solicitados
    
    # Verificar límite de 30 días
    if total_dias > MAX_LICENCIA_ANUAL:
        return f"""## Solicitud de Licencia Denegada

**Empleado:** {employee['Nombre Completo']}
**Días ya gozados:** {dias_actuales}
**Días solicitados:** {dias_solicitados}
**Total:** {total_dias} días

**Error:** No se puede tomar más de {MAX_LICENCIA_ANUAL} días de licencia por año.

**Opciones disponibles:**
- Contactar al corresponsal de recursos humanos
- Enviar un email a **rrhh@ibm.com** con el motivo de la solicitud especial

**Email sugerido:** rrhh@ibm.com"""
    
    # Actualizar días de licencia
    employees = _load_employees()
    for emp in employees:
        if ((nombre_completo_empleado and emp["Nombre Completo"].strip().lower() == nombre_completo_empleado.strip().lower()) or
            (numero_empleado and emp["Número de Empleado"].strip() == str(numero_empleado).strip())):
            emp["Días de Licencia"] = str(total_dias)
            break
    
    _save_employees(employees)
    
    return f"""## Solicitud de Licencia Aprobada

**Empleado:** {employee['Nombre Completo']}
**Período de Licencia:** {fecha_inicio} - {fecha_fin}
**Días Solicitados:** **{dias_solicitados}** días
**Total Días Gozados:** **{total_dias}** días
**Días Restantes:** **{MAX_LICENCIA_ANUAL - total_dias}** días

Su solicitud de licencia ha sido aprobada y registrada exitosamente."""