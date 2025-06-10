# 🛠️ Configuración de Casos de Uso - Bootcamp de IA Agéntica

## 📖 Tabla de Contenidos
- [🛠️ Configuración de Casos de Uso - Bootcamp de IA Agéntica](#️-configuración-de-casos-de-uso---bootcamp-de-ia-agéntica)
  - [📖 Tabla de Contenidos](#-tabla-de-contenidos)
  - [📖 Descripción](#-descripción)
  - [📁 Estructura del Proyecto](#-estructura-del-proyecto)
  - [🚀 Inicio Rápido](#-inicio-rápido)
    - [1. Configuración del Entorno](#1-configuración-del-entorno)
    - [2. Backend del Primer Laboratorio](#2-backend-del-primer-laboratorio)
  - [📋 Prerrequisitos](#-prerrequisitos)
  - [🎯 Objetivos del Setup](#-objetivos-del-setup)
  - [🆘 Soporte](#-soporte)
  - [📚 Recursos Adicionales](#-recursos-adicionales)


## 📖 Descripción

Este directorio contiene todos los recursos necesarios para la configuración inicial del **Bootcamp de IA Agéntica**. Incluye guías paso a paso para la preparación del entorno, configuración de credenciales y backend de ejemplo para el primer laboratorio.

## 📁 Estructura del Proyecto

```
usecase-setup/
├── README.md                          # Este archivo
├── environment-setup/                 # Configuración del entorno
│   ├── 1_crear-IBMid.md              # Crear cuenta IBM ID
│   ├── 2_acceder-a-los-entornos.md   # Acceso a entornos de clase
│   ├── 3_crear-projecto.md           # Creación de proyecto en Watsonx
│   └── assets/                        # Imágenes y recursos
└── lab-1-agente-rrhh/                # Backend para el primer lab
    ├── rrhh_backend_api/              # API REST para RRHH
    └── rrhh_backend_mcp/              # MCP Server para RRHH
```

## 🚀 Inicio Rápido

### 1. Configuración del Entorno

Sigue estos pasos en orden para configurar tu entorno de trabajo:

1. **[Crear IBMid](environment-setup/1_crear-IBMid.md)** - Crear tu cuenta IBM (solo para Socios y Clientes)
2. **[Acceder a Entornos](environment-setup/2_acceder-a-los-entornos.md)** - Aceptar invitación y acceder a la cuenta
3. **[Crear Proyecto](environment-setup/3_crear-projecto.md)** - Configurar proyecto en WatsonX

### 2. Backend del Primer Laboratorio

El directorio `lab-1-agente-rrhh/` contiene dos implementaciones de backend:

- **`rrhh_backend_api/`** - API REST con FastAPI para gestión de recibos de sueldo
- **`rrhh_backend_mcp/`** - Model Context Protocol (MCP) Server para integración con agentes

## 📋 Prerrequisitos

- **IBMid** - Cuenta de IBM válida
- **Acceso a TechZone** - Invitación aceptada al entorno de clase
- **Python 3.11+** - Para ejecutar los backends localmente
- **Docker** (opcional) - Para despliegue containerizado

## 🎯 Objetivos del Setup

Al completar esta configuración tendrás:

- ✅ Cuenta IBM configurada y acceso al entorno
- ✅ Proyecto en Watsonx.ai creado y configurado
- ✅ Credenciales y API keys generadas
- ✅ Backend de ejemplo funcionando para el Lab 1

## 🆘 Soporte

Si encuentras problemas durante la configuración:

1. Revisa las capturas de pantalla en `environment-setup/assets/`
2. Verifica que estés en la instancia correcta de TechZone
3. Asegúrate de tener un IBMid válido antes de aceptar invitaciones

## 📚 Recursos Adicionales

- [IBM TechZone](https://techzone.ibm.com/)
- [Watsonx.ai](https://dataplatform.cloud.ibm.com/wx/home)
- [IBM Cloud](https://cloud.ibm.com/)

---

**Nota:** Este setup es específico para el Bootcamp de IA Agéntica. Los empleados de IBM pueden usar sus credenciales corporativas directamente.
