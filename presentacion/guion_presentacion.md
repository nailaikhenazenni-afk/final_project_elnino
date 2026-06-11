Presentation: 

Diapositiva 1: Portada
Título del Proyecto: Análisis histórico de eventos del niño basado sobre variaciones del viento y la temperatura 
Nombre: Naila Ikhenazen Bouzid

Subtexto: Análisis de datos, contrucción de KPIs

Diapositiva 2: Descripción General del Proyecto

Introducción al problema: 

- El aumento de la temperatura superficial del mar (SST) junto con variaciones extremas de los vientos asociados a eventos de El Niño aleja a ciertas especies marinas comerciales de sus zonas habituales de captura.

Objetivo: 
icono flecha hacia abajo

- Crear un Dashboard de datos históricos sobre variaciones del viento y la temperatura del Pacífico para ayudar a empresas vulnerables al clima (como pesqueras y aseguradoras marítimas) a anticipar pérdidas y gestionar sus riesgos operativos.


Diapositiva 3: Dataset y Preparación de Datos
Origen de los datos:

- Dataset de Kaggel El Niño: recopila registros oceanográficos provenientes de la red de boyas (nota para mi se trata de una especie de balisas que registran los datos) del programa TOGA/TAO en el Pacífico tropical. 

Características clave:

Ausencia de valores nulos:

- No hay valores faltantes en el dataset.

Procesamiento y formato:

Editamos y aplicamos transformaciones básicas de formato, para asegurar una lectura ágil y eficiente de los datos, y así facilitar su manejo.  (nota para mi)
Texto  para la diapositiva:
- Edición y aplición de transformaciones básicas de formato ícono flecha  asegurar una lectura ágil y eficiente de los datos

Diapositiva 4: Selección de Variables Base

Nota para mi 

Selcionamos variables relacionadas con la temperatura del mar y el viento, ya que son los principales indicadores de eventos de El Niño y tienen un impacto directo en la distribución de las especies marinas, algo que interesa a las empresas pesqueras y aseguradoras.  

Es importante demostrar que estas se correlan entre sí y analizar también como lo hacen, además de su comportamiento histórico, podemos ayudar a las compañías a anticipar estos eventos. 

También podría ser el primer paso para construir un modelo predictivo que permitiría anticipar eventos extremos, lo que es crucial para la toma de decisiones en estas industrias. Eso en  el futuro

Texto diapositiva: ( la diapositiva ira dividida en dos partes en una van las variables en otra las explicaciones)

variables:

- Temperatura superficial del mar del día actual (sst_today) por coordenada
- Viento zonal (zonal_wind) del día por coordenada
- Promedio de temperatura de los últimos 15 días(sst_avg_fortnight) por coordenada
- Viento máximo de los últimos 15 días (wind_max_fortnight) por coordenada
- viento promedio de los últimos 15 días (avg_zonal_wind_15d) por coordenada
nota para mi las tres últimas variables las cree yo, para profundizar el analásis no venían en el Daset 

Criterio de selección:

 Selción de variables relacionadas con la temperatura del mar y el viento:

 -> principales indicadores de eventos de El Niño
 -> interesan a las empresas pesqueras y aseguradoras

  Importante:

 - demostrar que se correlan entre sí
 - analizar como lo hacen / comportamiento histórico
 (icono flecha hacia abajo)

  Ayudar las compañias a anticipar estos eventos


Diaposistiva 5: Visualización y análisis de las variables

La partimos en dos una parte par las imagenes otra para el texto explicativo

     (texto)
 - Determinación del Umbral riesgo >28, alerta temperatura demasiado elevada:
 - Media: 27.72
 - Mediana: 28.29
 - Umbral crítico de 28 °C demostrado de manera científica: Punto de inflexión térmico que activa tormentas masivas y altera las corrientes de pesca tradicionales* (añadir biblio al pie de la diapo).  (nota para mi: he investigado un poco para ver si iba por buen camino y he encontrado une estudio sobre esto)

 (imágen)
 histograma Distribución de la Temperatura Superficial del Mar (SST) en el Pacífico ( nota para mi no incluir en la diapo  clara asimetría negativa. El núcleo de las observaciones se concentra en un rango de entre 28°C y 29.5°C coerente con el clima de la región. Pico significativo por encima de los 30°C que puede ser asociado con los eventos más agudos de El Niño )
 

Diapositiva 6: Correlación

La partimos en dos una parte par las imagenes otra para el texto explicativo

Imágenes 

mapa de calor: Mapa de Calor: Dinámica Océano-Atmósfera

gráfica de dispersión 

(texto)

Correlación entre variables de viento y temperatura (icono check)

(nota para mi intentar pasar rapidamenente en estas dos)

Diapositiva 7:  KPI

 (Calculamos KPIs de riesgo que luego veromos en el Dashboard. nota para mi)

1. KPI de Riesgo por Temperatura del Mar (kpi_temp_risk): Proporción de días en los últimos 15 días donde la temperatura del mar (sst_avg_fortnight) superó un umbral crítico (28°C)

2. KPI de Riesgo de Viento (kpi_wind_risk): mide la inestabilidad de la atmósfera basada en la Desviación típica del viento zonal

3. KPI de Frecuencia de Eventos Extremos (kpi_extreme_events): Número de eventos extremos registrados en los últimos 14 días, definidos como días donde tanto la temperatura del mar superó el umbral crítico como el viento máximo superó su umbral crítico. (nota para mi: la idea es de  proporcionar una medida integrada del riesgo combinado de temperatura y viento.)

4.  KPI de Alerta Temprana (kpi_early_warning) que combine los indicadores de temperatura del día y viento para proporcionar una señal de alerta temprana 

( nota para mi el objetivo detrás de estos KPIS es permitir a las empresas pesqueras y aseguradoras marítimas monitorear de manera proactiva las condiciones del océano y tomar decisiones informadas para mitigar los riesgos asociados con eventos de El Niño.)

Diapositiva 8: Dashbord

capturas de pantanlla del dashbord

(nota para mi: ahora pasamos a ver al dashbord)

(nota para mi explcación del Dashboard: Relación entre Temperatura del Mar y Viento Máximo, variables al base nuetra kpi alerta temprana en cuando la velocidad del viento supera valores de 0 m/s y por lo tanto cambia de dirección la temperatura empieza también a aumentar y superar el umbral de riesgo deviación del viento, enseñar el valor de la desviación y decir que es muy alto, si comparamos con la media -3.30, mostrar el mapa dispersción: temperatura media quincenal, viento máximo qunincenal, valores a la base de nuestra KPI eventos Extremos. Alrta temprana y Alerta Eventos Extremos se superponen perfectamente justifica su pertinencia ya que una Alerta conduce invariablemente a eventos extremos  Los Eventos Extremos reperentan el 10,95 del total de los registros, valor alto. También fuerte correlación entre Temperatura Alta y Eventos Extremos ) 

Diapositiva 9: Resultados claves & Insights

Si hace falta partir la diapo en dos

(nota para mi: el análisis de los KPIs revela:) 

-  Riesgo de Eventos Extremos (KPI 3) significativo: un 10.95% (negrita) de ocurrencia histórica:
-> justifica la necesidad de sistemas de monitorización y alertas predictivas para las empresas pesqueras y aseguradoras marítimas.

- El KPI de Alerta Temprana (KPI 4): detecta anomalías concurrentes en el viento y la temperatura antes de que se consoliden en eventos extremos (nota para mi no incluir demuestra ser un indicador valioso) 

- La visualización de los KPIs confirma la relación de causa y efecto entre el comportamiento del viento y la temperatura del mar: 
 - Un cambio en el rumbo del viento conduce a la elevación de la temperatura del mar
 - La elevación de la temperatura del mar está correlacionada con el aumento del Riesgo de Eventos Extremos: del Niño
-> Subraya la importancia de los KPIs Alerta Intensidad del Viento y Alerta Temperatura Elevada
-> valida la utilidad de nuestro análisis para monitorear
                                               predecir  -> eventos de El Niño 
                                                         -> gestionar los riesgos asociados 


Diapositiva 10: Conclusión y futuros pasos

Partida en dos 

Conclución

- Probamos la utilidad de nuestro análisis para predicir en un futuro eventos de El Niño gracias a la monitorización y vigilencia del viento y de la temperatura del oceano
-> Permitira a las compañias pesqueras y aseguradoras gestionar los riesgos asociados de manera proactiva.

Futuros Pasos 

- Modelos predictivos
- Otras pistas de análisis: ej que especies marínas son las más afectadas por estos eventos

imágenes

curva regresión logística 

etiqueta con el resulado del random forest:  0.72 (72%)

(nota para mi: Probamos estos modelos los resultados no han sido muy concluyentes, más datos, modelos más avanzados, si hay tiempo explicar que el caso sobre todo para el ramdom forest, si preguntan nuestras columnas predictoras son: 'zonal_winds',
    'meridional_winds' y 'avg_zonal_wind_15d', y predicimos KPI Alerta Riesgo; Para la Regresión logística el resultado si que encaja al menos con nuestro análisis, predicimos KPI Alerta Riesgo según 'wind_max_fortnight' y llegamos a la conclución de que Si el viento llega a 0 m/s, la probabilidad de un evento extremo aumenta instantáneamente y además de manera significativa, teniendo estos datos las aseguradoras y las coompañias pesquera podrián actuar con días de antelación)

Diapositiva 11 Cierre
(1 slide):
Mi nombre 
 "Gracias", Comentarios/Preguntas.