import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Presentación El Niño", layout="wide")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main { background-color: #fdfaf4; }
    .stButton>button { width: 100%; border-radius: 20px; border: 1px solid #005088; }
    .title-text { color: #005088; font-family: 'Merriweather', serif; font-size: 50px; font-weight: bold; }
    .kpi-box { background-color: #ffffff; padding: 20px; border-radius: 15px; border-left: 5px solid #11caa0; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); margin-bottom: 10px; }
    .highlight { color: #d32f2f; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE NAVEGACIÓN ---
if 'slide' not in st.session_state:
    st.session_state.slide = 0

def next_slide(): st.session_state.slide += 1
def prev_slide(): st.session_state.slide -= 1

# --- CONTENIDO DE LAS DIAPOSITIVAS ---

def slide_0(): # PORTADA
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #005088;'>Análisis histórico de eventos del niño basado sobre variaciones del viento y la temperatura</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Naila Ikhenazen Bouzid</h3>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='text-align: center; font-size: 20px;'>Análisis de datos | Construcción de KPIs</p>", unsafe_allow_html=True)

def slide_1(): # DESCRIPCIÓN GENERAL
    st.header("Descripción General del Proyecto")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Introducción al problema")
        st.write("El aumento de la temperatura superficial del mar (SST) junto con variaciones extremas de los vientos asociados a eventos de El Niño aleja a ciertas especies marinas comerciales de sus zonas habituales de captura.")
    with col2:
        st.subheader("🎯 Objetivo")
        st.info("Crear un Dashboard de datos históricos para ayudar a empresas vulnerables (pesqueras y aseguradoras) a anticipar pérdidas y gestionar sus riesgos operativos.")

def slide_2(): # DATASET
    st.header("Dataset y Preparación de Datos")
    st.subheader("📍 Origen de los datos: Kaggle (TOGA/TAO)")
    st.write("Registros provenientes de la red de boyas del programa TOGA/TAO en el Pacífico tropical.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("✅ **Ausencia de valores nulos:** Dataset íntegro y completo.")
    with col2:
        st.write("**Procesamiento:**")
        st.write("Edición y aplicación de transformaciones básicas de formato ➡️ Lectura ágil y eficiente.")

def slide_3(): # SELECCIÓN VARIABLES
    st.header("Selección de Variables Base")
    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.markdown("""
        **Variables Clave:**
        - `sst_today`: Temp. actual
        - `zonal_wind`: Viento zonal
        - `sst_avg_fortnight`: Promedio 15d (SST)
        - `wind_max_fortnight`: Viento Máx 15d
        - `avg_zonal_wind_15d`: Viento Promedio 15d
        """)
    with col2:
        st.subheader("Criterio de selección")
        st.write("Seleccionamos variables de mar y viento por ser los principales indicadores de El Niño e impactar directamente en la distribución de especies.")
        st.warning("📊 Importante: Demostrar correlación y comportamiento histórico para anticipar eventos extremos.")

def slide_4(): # VISUALIZACIÓN
    st.header("Visualización y Análisis de Variables")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Análisis Estadístico:**")
        st.write("- Media: 27.72 | Mediana: 28.29")
        st.error("🚨 Umbral crítico: > 28°C (Científicamente demostrado)")
        st.caption("Biblio: Graham & Barnett (1987); Sud et al. (1995)")
    with col2:
        st.write("📈 *Aquí iría tu histograma de distribución SST*")
        # Simulación de gráfica
        st.bar_chart(np.random.normal(28, 1, 100))

def slide_5(): # CORRELACIÓN
    st.header("Correlación: Dinámica Océano-Atmósfera")
    col1, col2 = st.columns(2)
    with col1:
        st.write("🖼️ [Imagen Mapa de Calor]")
    with col2:
        st.write("🖼️ [Imagen Gráfica de Dispersión]")
    st.success("✔️ Correlación confirmada entre variables de viento y temperatura.")

def slide_6(): # KPIs
    st.header("Indicadores Clave de Riesgo (KPIs)")
    kpis = [
        ("1. Riesgo Temp.", "SST > 28°C en últimos 15 días."),
        ("2. Riesgo Viento", "Inestabilidad basada en Desviación Típica."),
        ("3. Eventos Extremos", "Combinación: Temp Crítica + Viento Máx Crítico."),
        ("4. Alerta Temprana", "Señal predictiva combinada para mitigación proactiva.")
    ]
    for titulo, desc in kpis:
        st.markdown(f"<div class='kpi-box'><b>{titulo}</b>: {desc}</div>", unsafe_allow_html=True)

def slide_7(): # DASHBOARD
    st.header("Exploración del Dashboard")
    st.write("🖼️ [Insertar Capturas de Pantalla de tu Dashboard]")
    st.info("💡 Insight: El viento cambia de dirección -> la temperatura aumenta -> superamos el umbral de riesgo.")

def slide_8(): # RESULTADOS
    st.header("Resultados claves & Insights")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Ocurrencia Histórica Eventos Extremos", "10.95%")
        st.write("- Justifica la necesidad de monitorización constante.")
    with col2:
        st.subheader("KPI Alerta Temprana")
        st.write("Detecta anomalías antes de que se consoliden. Permite actuar con una ventana de tiempo crucial.")

def slide_9(): # CONCLUSIÓN
    st.header("Conclusión y Futuros Pasos")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Conclusión")
        st.write("La vigilancia del viento y temperatura permite gestionar riesgos de manera proactiva en el sector pesquero.")
    with col2:
        st.subheader("Futuros Pasos")
        st.write("- Modelos predictivos avanzados.")
        st.write("- Análisis de impacto por especies específicas.")

def slide_10(): # CIERRE
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.balloons()
    st.markdown("<h1 style='text-align: center;'>¡Muchas Gracias!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Naila Ikhenazen Bouzid</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>¿Preguntas o comentarios?</p>", unsafe_allow_html=True)

# --- RENDERIZADO ---
slides = [slide_0, slide_1, slide_2, slide_3, slide_4, slide_5, slide_6, slide_7, slide_8, slide_9, slide_10]

# Barra lateral de navegación
st.sidebar.title("Navegación")
progress = (st.session_state.slide + 1) / len(slides)
st.sidebar.progress(progress)
st.sidebar.write(f"Diapositiva {st.session_state.slide + 1} de {len(slides)}")

col_nav1, col_nav2 = st.sidebar.columns(2)
if st.session_state.slide > 0:
    col_nav1.button("⬅️ Anterior", on_click=prev_slide)
if st.session_state.slide < len(slides) - 1:
    col_nav2.button("Siguiente ➡️", on_click=next_slide)

# Mostrar la diapositiva actual
slides[st.session_state.slide]()