# 🧪 Guía Lab 2 - Agente de Automatización de Negocios

![](./assets/ba_landscape.jpg)

Uno de los principales desafíos que enfrentan las organizaciones modernas es la dependencia de procesos manuales para tareas críticas como la investigación de mercado, el análisis competitivo y la generación de propuestas comerciales. Estos enfoques tradicionales no solo consumen tiempo y recursos, sino que también limitan la capacidad de respuesta ante cambios rápidos en el entorno competitivo. La falta de automatización impide acceder a información actualizada en tiempo real, lo que debilita el posicionamiento estratégico y reduce la efectividad de los equipos comerciales. En un entorno empresarial cada vez más dinámico, la automatización inteligente se vuelve esencial para mejorar la productividad, acelerar la toma de decisiones y mantener una ventaja competitiva sostenible.

## 📖 Tabla de Contenido

- [🧪 Guía Lab 2 - Agente de Automatización de Negocios](#-guía-lab-2---agente-de-automatización-de-negocios)
  - [📖 Tabla de Contenido](#-tabla-de-contenido)
  - [🤔 El Problema](#-el-problema)
  - [🎯 Objetivo](#-objetivo)
  - [📈 Valor Empresarial](#-valor-empresarial)
  - [🏛️ Arquitectura](#️-arquitectura)
  - [📄 Laboratorio práctico paso a paso](#-laboratorio-práctico-paso-a-paso)
    - [Creación Agente Comparador en Watsonx.ai](#creación-agente-comparador-en-watsonxai)
      - [Crear Proyecto y Asociar instancia de Machine Learning](#crear-proyecto-y-asociar-instancia-de-machine-learning)
    - [Watsonx Orchestrate](#watsonx-orchestrate)
    - [Testear](#testear)
  - [🎥 Demostración](#-demostración)

## 🤔 El Problema

El departamento de ventas de ABC Motors enfrentó desafíos al preparar propuestas comerciales para su nueva línea de vehículos de alto rendimiento. Cada vez que lanzan un nuevo modelo, el equipo de análisis competitivo dedica una gran cantidad de tiempo y recursos para entregar sus conclusiones. Los problemas incluyen:
- La investigación manual retrasa la toma de decisiones y reduce la productividad.
- Un posicionamiento débil dificulta la diferenciación en ventas.
- La respuesta lenta a los cambios del mercado, debido a la falta de inteligencia en tiempo real.

## 🎯 Objetivo

ABC Motors planea implementar un Sistema de Inteligencia Competitiva impulsado por IA para automatizar la investigación de mercado y el análisis de la competencia. Este sistema ayudará a los equipos de ventas a identificar y posicionar rápidamente sus productos frente a los competidores, superando la falta de eficiencia de la investigación manual y los análisis desactualizados. El objetivo es crear un sistema habilitado por IA que respalde el análisis competitivo y la investigación de mercado mediante:
- Extraer productos del catálogo de productos de la empresa.
- Identificar y extraer las características clave de cada producto.
- Buscar productos de la competencia basándose en atributos clave.
- Generar una tabla comparativa estructurada con precios, características y diferenciadores.
- Realizar un análisis FODA (Fortalezas, Oportunidades, Debilidades y Amenazas) para ofrecer una visión estratégica más profunda.

Al automatizar estas tareas, la empresa logra acelerar los procesos de ventas, mejorar la precisión de los datos y permitir que los equipos de ventas tomen decisiones informadas con mayor rapidez.

## 📈 Valor Empresarial

- Reducción del tiempo dedicado a la investigación manual de la competencia.
- Actualizaciones automáticas y en tiempo real sobre la competencia en el mercado.
- Mejora en la efectividad del discurso de ventas.

## 🏛️ Arquitectura
Para ejecutar un proceso de análisis competitivo, se ha diseñado un Multi-Agente de Inteligencia Artificial que, de manera autónoma, extrae y analiza información sobre los productos internos del [Catálogo de productos ABC Motors](./docs/Catalogo%20de%20productos%20de%20ABC%20Motor.pdf). El uso de un sistema basado en un Multi-Agente de IA garantiza eficiencia, precisión y respuestas en tiempo real para los equipos de estrategia y ventas. La arquitectura consiste en Agentes de IA especializados, trabajando de manera conjunta para lograr las siguientes funcionalidades:
- Extraer productos del catálogo de productos interno
- Extraer características y detalles de los productos del catálogo de productos interno
- Buscar productos competidores
- Generar una comparación con la competencia, en un formato estructurado
- Generar un análisis FODA (Fortalezas, Oportunidades, Debilidades y Amenazas)

![](./assets/Business_Automation_Architecture.png)

Este caso de uso, utiliza las capacidades de los agentes de Watsonx Orchestrate para extraer información específica (como el nombre y sus características, por ejemplo) de los productos del catalogo. Además, se utiliza un Agente de IA externo, desplegado en Watsonx.ai, capaz de realizar una búsqueda de productos competidores y de compararlos con los productos del catálogo de productos interno. 

- **Product Agent:** Este agente se encarga de responder todas las consultas relacionadas con los productos de la empresa. Es responsable de buscar un producto específico y retornar los detalles y características principales en un formato estructurado desde el catalogo de productos. Asegura la entrega de respuestas claras y concisas, haciendo más fácil el entendimiento y uso del agente. Adicionalmente, delega tareas al Agente Comparador para un procesamiento adicional de la información
- **Agente Comparador:** Este agente se encarga del proceso completo de comparación de productos. Primero realiza una recolección de URLs de los productos similares basándose en las características principales. Luego, usando esos URLs, analiza el producto competidor, extrae la información clave y genera un análisis FODA para cada producto. Los resultados se presentan de una manera clara y estructurada en una tabla, permitiendo una rápida comparación y análisis.

## 📄 Laboratorio práctico paso a paso

A continuación se detallan los pasos necesarios para ejecutar el Laboratorio.

### Creación Agente Comparador en Watsonx.ai

#### Crear Proyecto y Asociar instancia de Machine Learning
1. Asociar instancia ML
2. Crear Deployment Space
3. Crear Agente con los siguientes campos:
   1. Nombre: Comparison Agent - AL
   2. Descripción: The agent compares the given data with additional information gathered from Google search results.
   3. Instrucciones:
```
You are an expert of automobile industry combining given details present in your context window.  Your task is crawl and search the Top 3 product URLs (strictly from the automobile industry) and to analyse and compare products on the following features strictly: Range, Pricing, Acceleration, Top Speed, Interior and Safety Features If a feature is not applicable, mark it as N/A. Additionally, perform a SWOT analysis of top products (Strengths, Weaknesses, Opportunities, and Threats) Present the comparison in 3 tables one for the comparison , second for the rating numerical rating (X/5) and a star rating (★ out of ★★★★★) for each feature  and  third for the SWOT analysis. Give heading to each table . After every table give two divider.
Instructions:
1. When asked for competitors of the given product, make sure that you provide only the name of the products and URLs of the products below the corresponding name.
2. The generated product URLs must be strictly from the automobile industry.
3. Title for Table 1: Feature Comparison
4. Title for Table 2: Rating Comparison
5. Make sure that the Rating Comparison table has both the numerical(X/5) and star rating(★ out of ★★★★★)
6. The products should be the column names in all the tables.
7.  The font of the Table Title must be bold and the font size must be 40% bigger as compared to the rest of the text.
8.  Add appropriate space between each section in the table.
9.  Name the References as Competitors
```
1. Guardar Agente
2. Desplegar
   1. En caso de no tener API key creada en el perfil, crearla.
3. Ir al despliegue y copiar el endpoint público de stream:

```
https://us-south.ml.cloud.ibm.com/ml/v4/deployments/6d10ee9f-4e08-4391-8982-744cdf2a6545/ai_service_stream?version=2021-05-01
```

### Watsonx Orchestrate
1. Ir a Agent Builder en wxo y darle crear agente
2. Poner nombre: Product Agent
3. Poner descripción: 

```
This agent is designed to search for a specified product and retrieve its details and features using Retrieval-Augmented Generation (RAG) on the product catalog. It presents the information in a clear and structured format, ensuring systematic organization of key product data, making it easy to understand and use.
```

4. En Knowledge, poner descripción: 

```
Your knowledge base is the document that contains all the product-related information. All queries related to the product will be addressed using this document as the primary source.
```

5. Agregar archivo de documentación
6. Agregar Agente desde la opción de Import
   1. Elegir opción de External Agent
   2. Provider: x.ai
   3. Api key: agregar una
   4. URL: url de stream de x.ai
   5. Name: Comparison_Agent_V1
   6. Descripción: 

```
Este agente está diseñado para buscar URLs competitivas del producto de entrada y comparar los datos con información adicional obtenida de los resultados de búsqueda de Google. Su tarea consiste en analizar cuidadosamente los datos de entrada, extraer información clave e identificar diferencias y similitudes. Los resultados deben presentarse en un formato de tabla bien estructurado, lo que facilita la comprensión y la comparación de la información a simple vista.
```

7. En Behavior, ponemos: 

```
This agent is responsible for handling product-related queries using Retrieval-Augmented Generation (RAG) on the product catalog. For general product queries, it retrieves structured information directly from the knowledge base. For queries involving URLs or web references or comparison, it delegates the task to the Comparison Agent.
```

### Testear

Preguntas base documental:

- What are the products of ABC Motors. Cuales son los productos de ABC Motors?

- Give me the info of Zenith X3. Dame la información del Zenith X3.

Preguntas para llamar Agente comparador:

- Give me URLs of the competitors of the above product and show me the comparison as well.
- Dame las URL de los competidores del producto mencionado anteriormente y muéstrame la comparación también.

## 🎥 Demostración

<video controls>
  <source src="./assets/demo.mov">
</video>