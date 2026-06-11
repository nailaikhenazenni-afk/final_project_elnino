import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Presentación El Niño", layout="wide")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main { background-color: #fdfaf4; }
    .stButton>button { width: 100%; border-radius: 20px; border: 1px solid #005088; background-color: #005088; color: white; }
    .stButton>button:hover { background-color: #11caa0; border: 1px solid #11caa0; }
    .title-text { color: #005088; font-family: 'Merriweather', serif; font-size: 50px; font-weight: bold; }
    .kpi-box { background-color: #ffffff; padding: 20px; border-radius: 15px; border-left: 5px solid #11caa0; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); margin-bottom: 10px; }
    .highlight { color: #d32f2f; font-weight: bold; }
    
    /* Métrica Gigante para los Eventos Extremos */
    .metric-container { background-color: #ffffff; padding: 20px; border-radius: 15px; border: 1px solid #e0e0e0; text-align: center; }
    .metric-title { font-size: 20px; color: #555555; }
    .metric-value { font-size: 50px; color: #005088; font-weight: bold; }

    /* Tarjeta/Etiqueta visual para el resultado de Random Forest */
    .rf-badge {
        background-color: #11caa0;
        color: white;
        padding: 15px 30px;
        border-radius: 50px;
        display: inline-block;
        font-size: 35px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(17, 202, 160, 0.3);
        margin: 10px 0;
        text-align: center;
        width: 100%;
    }
    .rf-label {
        font-size: 18px;
        color: #005088;
        font-weight: bold;
        margin-bottom: 5px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE NAVEGACIÓN ---
if 'slide' not in st.session_state:
    st.session_state.slide = 0

def next_slide(): st.session_state.slide += 1
def prev_slide(): st.session_state.slide -= 1
def go_to_slide(n): st.session_state.slide = n

# --- CONTENIDO DE LAS DIAPOSITIVAS ---

def slide_0(): # PORTADA
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #005088;'>Análisis histórico de eventos del niño basado sobre variaciones del viento y la temperatura</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Naila Ikhenazen Bouzid</h3>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='text-align: center; font-size: 20px;'>Análisis de datos | Construcción de KPIs</p>", unsafe_allow_html=True)


def slide_1(): # ÍNDICE
    st.header("📋 Índice de la Presentación")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        1. **Descripción General** (Introducción y Objetivos)
        2. **Dataset** (Origen y Preparación)
        3. **Selección de Variables** (Criterios e Indicadores)
        4. **Visualización** (Análisis Estadístico)
        5. **Correlación** (Dinámica Océano-Atmósfera)
        """)
    with col2:
        st.markdown("""
        6. **KPIs** (Indicadores de Riesgo)
        7. **Dashboard** (Exploración Visual)
        8. **Resultados** (Key Insights)
        9. **Conclusiones y Modelos** (Predicción Futura)
        10. **Cierre**
        """)


def slide_2(): # DESCRIPCIÓN GENERAL
    st.header("1. Descripción General del Proyecto")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Introducción al problema")
        st.write("El aumento de la temperatura superficial del mar (SST) junto con variaciones extremas de los vientos asociados a eventos de El Niño aleja a ciertas especies marinas comerciales de sus zonas habituales de captura.")
    with col2:
        st.subheader("🎯 Objetivo")
        st.info("Crear un Dashboard de datos históricos sobre variaciones del viento y la temperatura del Pacífico para ayudar a empresas vulnerables al clima (como pesqueras y aseguradoras marítimas) a anticipar pérdidas y gestionar sus riesgos operativos.")


def slide_3(): # DATASET
    st.header("2. Dataset y Preparación de Datos")
    st.subheader("🌐 Origen de los datos: Kaggle (El Niño)")
    st.write("Recopila registros oceanográficos provenientes de la red de boyas (balizas que registran las variables) del programa TOGA/TAO en el Pacífico tropical.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("✅ **Ausencia de valores nulos:** No hay valores faltantes en el dataset, asegurando un análisis consistente.")
    with col2:
        st.subheader("Procesamiento y formato")
        st.write("Edición y aplicación de transformaciones básicas de formato ➡️ Asegurar una lectura ágil y eficiente de los datos.")


def slide_4(): # SELECCIÓN VARIABLES
    st.header("3. Selección de Variables Base")
    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.markdown("""
        **Variables Clave Seleccionadas:**
        - `sst_today`: Temperatura superficial del mar del día actual por coordenada.
        - `zonal_wind`: Viento zonal del día por coordenada.
        - `sst_avg_fortnight`: Promedio de temperatura de los últimos 15 días por coordenada.
        - `wind_max_fortnight`: Viento máximo de los últimos 15 días por coordenada.
        - `avg_zonal_wind_15d`: Viento promedio de los últimos 15 días por coordenada.
        """)
        st.caption("*Nota: Las tres últimas variables fueron calculadas a partir del dataset original para profundizar en las dinámicas quincenales.")
    with col2:
        st.subheader("Criterio de selección")
        st.write("Selección de variables directamente relacionadas con la temperatura del mar y el viento por ser los indicadores clave de eventos de El Niño, impactando la distribución de recursos biológicos de interés para pesqueras y aseguradoras.")
        st.warning("👁️ **Importante:** Analizar el comportamiento histórico y demostrar la correlación mutua para ayudar a las compañías a anticipar anomalías.")


def slide_5(): # VISUALIZACIÓN
    st.header("4. Visualización y Análisis de Variables")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Análisis Estadístico de la SST")
        st.write("- **Media:** 27.72 °C")
        st.write("- **Mediana:** 28.29 °C")
        st.error("🚨 **Umbral crítico determinado:** > 28 °C")
        st.write("Demostrado científicamente como el punto de inflexión térmico que activa tormentas masivas y altera de manera drástica las corrientes de pesca tradicionales.")
        st.caption("*Bibliografía al pie: Graham & Barnett (1987); Sud et al. (1995).")
    with col2:
        try:
            st.image(r'imagenes/histogram.png', caption="Distribución de la Temperatura Superficial del Mar (SST)")
        except Exception:
            st.warning("Gráfica 'histogram.png' no encontrada en la carpeta 'imagenes'.")


def slide_6(): # CORRELACIÓN
    st.header("5. Correlación: Dinámica Océano-Atmósfera")
    col1, col2 = st.columns(2)
    with col1:
        try:
            st.image(r'imagenes/mapa_calor.png', caption="Mapa de Calor: Dinámica Océano-Atmósfera")
        except Exception:
            st.warning("Imagen 'mapa_calor.png' no encontrada.")
    with col2:
        try:
            st.image(r'imagenes/grafica_dispersion.png', caption="Gráfica de Dispersión entre Viento y Temperatura")
        except Exception:
            st.warning("Imagen 'grafica_dispersion.png' no encontrada.")
    st.success("✔️ Correlación robusta confirmada entre las variables de velocidad del viento y anomalías de temperatura.")


def slide_7(): # KPIs
    st.header("6. Indicadores Clave de Riesgo (KPIs)")
    st.write("Cálculo y formulación de las métricas de riesgo que integran el cuadro de mando:")
    
    kpis = [
        ("1. KPI de Riesgo por Temperatura del Mar (kpi_temp_risk)", "Proporción de días en los últimos 15 días donde la temperatura promedio superó el umbral crítico de 28°C."),
        ("2. KPI de Riesgo de Viento (kpi_wind_risk)", "Mide la inestabilidad de la atmósfera basada en la Desviación Típica del viento zonal (Punto de referencia: Media histórica de -3.30 m/s)."),
        ("3. KPI de Alerta de Eventos Extremos (kpi_extreme_events)", "Número de eventos conjuntos registrados en los últimos 15 días donde tanto la SST pormedia quincenal como el viento máximo superaron sus respectivos umbrales críticos."),
        ("4. KPI de Alerta Temprana (kpi_early_warning)", "Indicador combinado que evalúa las condiciones del día actual junto a la tendencia del viento para generar señales proactivas de alarma.")
    ]
    for titulo, desc in kpis:
        st.markdown(f"<div class='kpi-box'><b>{titulo}</b>:<br>{desc}</div>", unsafe_allow_html=True)


def slide_8(): # DASHBOARD
    st.header("7. Exploración del Dashboard Dashboard")
    col1, col2 = st.columns(2)
    with col1:
        try:
           st.image(r'imagenes/capatura_pantalla_dashboard1.jpg', caption="Vista General del Cuadro de Mando - Control de KPIs", use_container_width=True)
        except Exception:
            st.warning("Imagen 'capatura_pantalla_dashboard1.jpg' no encontrada.")
    with col2:
        try:
        
            st.image(r'imagenes/captura_pantalla_dashboard2.png', caption="Análisis de Tendencias Coordenadas y Dispersión", use_container_width=True)
        except Exception:
            st.warning("Imagen 'captura_pantalla_dashboard2.png' no encontrada.")

def slide_9(): # RESULTADOS
    st.header("8. Resultados claves & Insights")
    col1, col2 = st.columns(2)
    with col1:
        st.info("💡 **Dinámica observada:** El viento cambia de dirección ➡️ la temperatura aumenta ➡️ superamos el umbral de riesgo.")
        
        # Componente de Métrica gigante personalizada
        st.markdown("""
            <div class='metric-container'>
                <div class='metric-title'>Ocurrencia Histórica de Eventos Extremos</div>
                <div class='metric-value'>10.95%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("Un porcentaje de ocurrencia significativo que justifica plenamente la necesidad de integrar alertas predictivas para la gestión de pérdidas.")
    with col2:
        st.subheader("KPI Alerta por Intensidad del Viento")
        st.write("Funciona como nuestra primera señal de alarma temprana en el sistema físico.")
        
        st.subheader("KPI Alerta Temprana")
        st.write("Detecta anomalías antes de que se consoliden. Permite actuar con una ventana de tiempo crucial.")
        st.subheader("KPI de Riesgo por Temperatura del Mar")
        st.write("👁️ **Importante:**  Fuerte correlación con eventos extremos.")


def slide_10(): # CONCLUSIÓN Y MODELOS
    st.header("9. Conclusión y Futuros Pasos")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📌 Conclusión")
        st.write("La vigilancia del viento y de latemperatura permite gestionar riesgos de manera proactiva y anticipar eventos anómalos de El Niño.")
        
        st.markdown("**Futuros Pasos:**")
        st.write("- Desarrollo e integración de modelos predictivos avanzados.")
        st.write("- Análisis de qué especies marinas comerciales son más afectadas por estas variaciones térmicas.")
        
    with col2:
        st.subheader("🤖 Evaluación de Modelos de Machine Learning")

        st.write("---")
        st.subheader("📈 Análisis con Regresión Logística")
        
        try:
            st.image(r'imagenes/regresion.png', caption="Curva de Ajuste de Regresión Logística")
        except Exception:
            st.warning("Imagen 'regresion.png' no encontrada.")
            
       
         # Etiqueta generada por código para el Random Forest
        st.markdown("""
            <div style='text-align: center; margin-top: 15px; margin-bottom: 15px;'>
                <div class='rf-label'>Precisión Global Obtenida</div>
                <div class='rf-badge'>72 % Accuracy</div>
            </div>
            """, unsafe_allow_html=True)
        

def slide_11(): # CIERRE
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.balloons()
    st.markdown("<h1 style='text-align: center; color: #005088;'>¡Muchas Gracias!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Naila Ikhenazen Bouzid</h3>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='text-align: center; font-size: 22px;'>¿Turno de preguntas, comentarios o aclaraciones?</p>", unsafe_allow_html=True)


# --- RENDERIZADO Y CONTROL DE FLUJO ---
slides = [
    slide_0, slide_1, slide_2, slide_3, slide_4, 
    slide_5, slide_6, slide_7, slide_8, slide_9, 
    slide_10, slide_11
]

# Estructura de navegación en la barra lateral
st.sidebar.title("Control de la Presentación")
st.sidebar.write(f"Diapositiva actual: {st.session_state.slide + 1} de {len(slides)}")

# Botones de paso secuencial
col_nav1, col_nav2 = st.sidebar.columns(2)
if st.session_state.slide > 0:
    col_nav1.button("⬅️ Anterior", on_click=prev_slide)
if st.session_state.slide < len(slides) - 1:
    col_nav2.button("Siguiente ➡️", on_click=next_slide)

# Accesos directos estratégicos para agilizar la exposición ante preguntas del tribunal
st.sidebar.write("---")
st.sidebar.write("**Saltos rápidos:**")
if st.sidebar.button("📜 Portada Principal"): go_to_slide(0)
if st.sidebar.button("📖 Índice de Contenidos"): go_to_slide(1)
if st.sidebar.button("📈 Resultados e Insights"): go_to_slide(9)
if st.sidebar.button("🤖 Conclusiones y Modelos"): go_to_slide(10)

# Lanzamiento de la función correspondiente a la diapositiva activa
slides[st.session_state.slide]()