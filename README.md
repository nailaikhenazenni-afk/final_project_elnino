# final_project_elnino

## Problema de negocio

El aumento de la temperatura superficial del mar (SST) junto con variaciones extremas de los vientos asociados a eventos de El Niño aleja a ciertas especies marinas comerciales de sus zonas habituales de captura.

---

## Objetivo del proyecto

Crear un Dashboard de datos históricos sobre variaciones del viento y la temperatura del Pacífico para ayudar a empresas vulnerables al clima (como pesqueras y aseguradoras marítimas) a anticipar pérdidas y gestionar sus riesgos operativos.

---

## Datasets utilizados

### 1.El Niño Dataset
Contiene:
 
- observation
- year 
- month 
- day 
- date 
- latitude 
- longitude 
- zonal_winds 
- meridional_winds 
- humidity 
- air_temp 
- sst

### 2. Dataset EL Niño Proyecto Final
Contiene:
- observation 
- latitude 
- longitude 
- zonal_winds 
- meridional_winds 
- sst 
- complete_date

### 3. Tabla Atmospheric Oceanic
Contiene:
- latitude 
- longitude
- complete_date 
- sst_today
- sst_avg_fortnight
- zonal_winds
- wind_max_fortnight
- meridional_winds
---

## Workflow del proyecto

Problema de negocio  
↓  
Hipótesis  
↓  
Enfoque analítico  
↓  
Comprensión de datos  
↓  
Limpieza de datos  
↓  
Transformación de datos  
↓  
EDA  
↓  
Análisis de KPIs  
↓  
Visualización y Dashboard  
↓  
Modelado predictivo (opcional)  
↓
Insights y Recomendaciones  

---

## Herramientas utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Tableau
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## KPIs analizados

: 
2. KPI de Riesgo de Viento (kpi_wind_risk): mide la inestabilidad de la atmósfera basada en la Desviación típica del viento zonal

3. KPI de Frecuencia de Eventos Extremos (kpi_extreme_events): Número de eventos extremos registrados en los últimos 14 días, definidos como días donde tanto la temperatura del mar superó el umbral crítico como el viento máximo superó su umbral crítico. Este KPI proporcionará una medida integrada del riesgo combinado de temperatura y viento.

4. También podríamos considerar la creación de un KPI de Alerta Temprana (kpi_early_warning) que combine los indicadores de temperatura y viento para proporcionar una señal de alerta temprana cuando se detecten condiciones que históricamente han precedido a eventos de El Niño, permitiendo a las empresas tomar medidas preventivas con mayor anticipación.

### KPI de Riesgo por Temperatura del Mar (kpi_temp_risk)
Proporción de días en los últimos 15 días donde la temperatura del mar (sst_avg_fortnight) superó un umbral crítico (por ejemplo, 28°C). Este KPI indicará el nivel de riesgo térmico para las operaciones pesqueras.


### Average Time Between Steps
Tiempo promedio entre pasos del proceso.

### Error Rate
Usuarios que retroceden pasos durante el proceso.

### Funnel Analysis
Abandono de usuarios a lo largo del flujo digital.

---

## Insights principales

- El grupo Test obtuvo una mayor tasa de finalización respecto al grupo Control.
- Existe una pérdida progresiva de usuarios a lo largo del funnel.
- Algunos pasos generan mayor fricción y abandono.
- El rediseño mejora el rendimiento general del proceso digital.

---

## Dashboard Tableau

El dashboard incluye:

- Completion Rate
- Comparación Test vs Control
- Funnel Analysis
- Average Time Between Steps
- Filtros interactivos
- Segmentación de usuarios

---

## Estructura del proyecto

```bash
final_project_elnino/
│
├── data/
│   ├── elnino.csv
│   ├── proyecto_final_elnino.csv
│   └── proyecto_final_elnino.db 
│   └── tabla_atmospheric_oceanic.csv
│
│   
├── notebooks/
│   ├── 01_proyecto_final_elnino.ipynb
│   ├── 02_sql_to_python.ipynb
│   ├── 03_machine_learning.ipynb
│   
│
├── tableau/
│
├── presentation/
│   ├── imagenes/
│   ├── guion_presentacion.md
│   ├── presentation.py
│   ├── requirements.txt│ 
│     
├── funcions.py
├── README.md
├── requirements.txt│ 
```

---

## Instalación

Clonar repositorio:

```bash
git clone https://github.com/yourusername/final_project_elnino.git
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar notebooks:

```bash
jupyter notebook
```

---

## Conclusiones

El análisis sugiere que el nuevo diseño digital mejora el rendimiento del proceso y genera una experiencia más eficiente para el usuario.

La variación Test superó al grupo Control en los principales KPIs del experimento.

---

## Próximos pasos

Posibles mejoras futuras:

- Segmentación avanzada
- Behavioral Analysis
- Session Path Analysis
- Power Analysis
- Modelos predictivos
- Streamlit App

---
