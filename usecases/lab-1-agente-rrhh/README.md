# 🧪 Guía Lab 1 - Agente Gestión de Recursos Humanos

<img alt="Agente Gestión de Recursos Humanos" src="assets/hr_landscape.jpg">

## 📖 Tabla de Contenidos
- [🧪 Guía Lab 1 - Agente Gestión de Recursos Humanos](#-guía-lab-1---agente-gestión-de-recursos-humanos)
  - [📖 Tabla de Contenidos](#-tabla-de-contenidos)
  - [🤔 El Problema](#-el-problema)
  - [🎯 Objetivo](#-objetivo)
  - [📈 Valor Empresarial](#-valor-empresarial)
  - [🏛️ Arquitectura](#️-arquitectura)
      - [Capacidades clave del Agente Gestión de Recursos Humanos:](#capacidades-clave-del-agente-gestión-de-recursos-humanos)
    - [Componentes de la Arquitectura](#componentes-de-la-arquitectura)
  - [🎥 Demostración](#-demostración)


Uno de los principales desafíos que enfrentan las grandes organizaciones es la gestión de sus operaciones de recursos humanos. A medida que las empresas crecen en tamaño, se vuelve cada vez más difícil obtener información de manera rápida y ejecutar tareas con facilidad. Con el auge de los sistemas agénticos y el poder de los modelos de razonamiento, se vuelve más sencillo tener un único punto de entrada para realizar prácticamente todas las operaciones de RRHH.

## 🤔 El Problema
TechCorp Inc., líder mundial en tecnología, enfrentó un desafío significativo en la gestión de sus crecientes operaciones de RRHH. A medida que la empresa se expandía, tuvo dificultades para manejar eficientemente los datos de perfiles de empleados, las solicitudes de tiempo libre y la gestión de la fuerza laboral. Los sistemas tradicionales de RRHH ya no eran suficientes para mantenerse al día con la escala y complejidad. Con múltiples herramientas de proveedores utilizadas para diferentes operaciones de RRHH, resulta difícil integrarlas todas y proporcionar una experiencia fluida al usuario.

## 🎯 Objetivo
El objetivo de este laboratorio es generar agentes externos personalizados y exportarlos a la plataforma de Watsonx Orchestrate, permitiendo su orquestación bajo un Agente principal. Se busca demostrar cómo programar un agente personalizado para casos avanzados y cómo Watsonx Orchestrate facilita la orquestación y el despliegue uniforme de estos agentes, integrando diversas herramientas y sistemas de gestión de RRHH en una solución centralizada y eficiente.

## 📈 Valor Empresarial
El uso de un sistema respaldado por IA para optimizar el proceso de RRHH puede tener impactos multidimensionales, como tiempo de resolución más rápido, mayor satisfacción del usuario, aumento de ingresos y reducción del agotamiento de empleados, lo que en última instancia impacta positivamente en el valor de su negocio. Por otro lado, aprovechar las capacidades agénticas traerá consigo su propio conjunto adicional de valores, como por ejemplo, mayor seguridad de datos y respuestas fundamentadas sin alucinaciones, mejorando así la experiencia de marca. 

## 🏛️ Arquitectura
Para agilizar las interacciones de los empleados con los sistemas de RRHH, hemos desarrollado dos agentes de Recursos Humanos que controlan diferentes aspectos de la unidad de negocio:

- **Agente de Recibos de Sueldo:** Conectado a una API tradicional, este agente permite a los empleados acceder de manera rápida y práctica a sus recibos de sueldo.

- **Agente de Operaciones de RRHH:** Encargado de la gestión de operaciones de Recursos Humanos, este agente se conecta a un servidor MCP (Model Context Protocol), facilitando todas las operaciones disponibles en el sistema al agente.

Ambos agentes están construidos utilizando el framework LangGraph y Watsonx.ai como motor de Inteligencia Artificial, y son desplegados en el servicio serverless IBM Code Engine, lo que permite disponibilizarlos globalmente. Finalmente, ambos agentes son orquestados por un agente matriz dentro de Watsonx Orchestrate, que gestiona todas las interacciones entre los usuarios, los agentes y el sistema en general.

#### Capacidades clave del Agente Gestión de Recursos Humanos:
1. Ver información de un empleado.
2. Consultar días de licencia gozada.
3. Solicitar días de licencia.
4. Actualizar el cargo de un empleado.
5. Actualizar la dirección de un empleado.
6. Obtener y visualizar el recibo de sueldo de un empleado.
7. Automatizar tareas rutinarias de RRHH como verificar el saldo de vacaciones y actualizar detalles de empleados.
8. Permitir interacción natural entre empleados y sistemas de RRHH backend a través de una interfaz de aplicación intuitiva.
9. Utilizar razonamiento y herramientas para obtener o actualizar información de manera segura y confiable.
10. Emplear Watsonx Orchestrate para coordinación, razonamiento avanzado y desarrollo de tareas, ofreciendo una experiencia integral de soporte de RRHH impulsada por IA.

### Componentes de la Arquitectura
- **Agente Orquestador Principal (IBM Watsonx Orchestrate)**: Actúa como el coordinador central que gestiona las interacciones de usuarios y delega tareas a los agentes especializados. Utiliza capacidades de razonamiento avanzado y desarrollo de tareas para ofrecer una experiencia integral de soporte de RRHH impulsada por IA. Este agente es definido dentro de la plataforma Watsonx Orchestrate.

- **Agente de Recibos de Sueldo**: Conectado a una API tradicional, este agente permite a los empleados acceder de manera rápida y práctica a sus recibos de sueldo y otra información relevante. Construido con el framework LangGraph y Watsonx.ai como motor de IA, desplegado en IBM Code Engine. Este agente es definido dentro de la carpeta rrhh-agente-api (`usecases/lab-1-agente-rrhh/rrhh-agente-api`).

- **Agente de Operaciones de RRHH**: Encargado de la gestión de operaciones de Recursos Humanos, este agente se conecta a un servidor MCP (Model Context Protocol), facilitando todas las operaciones disponibles en el sistema. Incluye capacidades para:
  - Ver información de empleados
  - Consultar y solicitar días de licencia
  - Actualizar cargo y dirección de empleados
  - Automatizar tareas rutinarias de RRHH
  - Construido con LangGraph y Watsonx.ai, desplegado en IBM Code Engine
Este agente es definido dentro de la carpeta rrhh-agente-api (`usecases/lab-1-agente-rrhh/rrhh-agente-api`).

- **Sistema de Gestión de Capital Humano (HCM)**: Sistema backend que almacena y gestiona todos los datos de empleados. Los agentes se comunican con este sistema para obtener o actualizar información, asegurando sincronización en tiempo real y precisión de datos. Consta de dos aplicaciones independientes: rrhh_backend_api (`usecases-setup/lab-1-agente-rrhh/rrhh_backend_api`) y rrhh_backend_mcp (`usecases-setup/lab-1-agente-rrhh/rrhh_backend_mcp`).


## 🎥 Demostración
_Aún no disponible_


> [!IMPORTANT]
> Este laboratorio utiliza un simulador para un sistema de Gestión de Capital Humano. Sin embargo, esto podría cambiarse fácilmente a cualquier sistema real que esté ejecutándose en producción como Workday u otros.