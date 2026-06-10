Presentation Structure:
Feel free to present the project in as you feel best represents your work, but below you will find a suggested format for the presentation as a guide.

Diapositiva 1: Portada
Título del Proyecto: Inteligencia Predictiva del fenómeno de El Niño: Machine Learning para la Mitigación del Riesgo Climático

Nombre: Naila Ikhenazen Bouzid

Subtexto: Implementación de Ciencia de Datos y Análisis Experto

Diapositiva 2: Descripción General del Proyecto
Introducción al problema: El fenómeno de El Niño es un patrón climático complejo que desencadena eventos meteorológicos extremos a nivel global. El diseño de este modelo aborda el problema como un desafío de clasificación supervisada para anticipar anomalías térmicas en el océano.

Objetivo: Desarrollar un modelo de Machine Learning capaz de predecir eventos de riesgo climatíco extremo, en determinadas coordenadas, para la Cadena de Suministro o Aseguradoras.

Impacto Potencial:  

Margen de 15 o 30 días  de anticipación para las empresas conserveras o de distribución pesquera, y así podrán anticipar la escasez de suministro y renegociar contratos de manera temprana. (nota para mí, no incluir esta parte en la presentación, es solo para mí esto sería más a nivel empresarial)


Mitigar los impactos socioeconómicos derivados de las crisis climáticas. (nota para mí, no incluir esta parte en la presentación, impacto más a nivel social)

Diapositiva 3: Dataset y Preparación de Datos
Origen de los datos: Dataset de Kaggel El Nino: recopila registros oceanográficos provenientes de la red de boyas del programa TOGA/TAO en el Pacífico tropical.

Características clave:

Ausencia de valores nulos: No hay valores faltantes en el dataset.

Procesamiento y formato: Solo editamos y aplicamos transformaciones básicas de formato, para asegurar una lectura ágil y eficiente de los datos, y así facilitar su manejo.

Diapositiva 4: Selección de Variables Base

Criterio de selección: Selección de variables según su importancia y capacidad para predecir el problema:

Latitud y longitud del lugar: Para saber la ubicación exacta de las boyas en el mapa.

Fecha: Para tener la información en su contexto y orden correcto a lo largo del tiempo.

Temperatura de la superficie del mar: El dato clave del agua que usamos para calcular cuándo saltará la alerta por anomalía (variable: alert_anomaly).

Vientos zonales (de este a oeste).

Vientos meridionales (de norte a sur).


Diapositiva 5: Creación de los indicadores basados en el tiempo (nuevas columnas nota para mí, no incluir esta parte en la presentación, es solo para mí esto es para explicar cómo se crean las nuevas columnas ):

Variable Objetivo (alert_anomaly): indica si la temperatura superficial del mar supera un umbral crítico, señalando una anomalía térmica.

El dato de la temperatura de hace 7 días (sst_lag_7)

El dato de la temperatura de hace 15 días sst_lag_15

: permiten dar más contexto a nuestro modelo de aprendizaje, así puede saber si el o .

Promedio de las últimas dos semanas (avg_sst_15d): Suaviza las fluctuaciones diarias de la temperatura superficial del mar, proporcionando una visión más clara de las tendencias térmicas a medio plazo.


Models Evaluation and Results
(1-2 slides):
Outline the types of models you experimented with and your rationale for selecting them.
Discuss the evaluation metrics and validation techniques used to assess model performance.
Model Optimization and correction
(1 slide):
Explain the hyperparameter tuning techniques employed (e.g., grid search, cross-validation).
Share insights on how these techniques improved your model's performance.
Key Findings and Insights
(2 slides):
Present the major findings from your model, potentially comparing different models or highlighting the most effective features.
Use visual aids to illustrate these insights clearly and effectively.
Real-World Application and Impact
(1 slide):
Discuss how your model can be applied in a real-world context and the potential impact it could have.
Consider any ethical considerations or limitations of your model.
Future Work and Improvements
(1 slide):
Suggest areas for future research or how the project could be expanded or improved with more time or resources.
Closing Slide
(1 slide):
Project title.
Team members' names.
A "Thank You" note, invitation for questions, or any final remarks.