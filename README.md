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

### KPI de Riesgo por Temperatura del Mar (kpi_temp_risk)
Proporción de días en los últimos 15 días donde la temperatura del mar (sst_avg_fortnight) superó un umbral crítico (por ejemplo, 28°C). Este KPI indicará el nivel de riesgo térmico para las operaciones pesqueras.

### KPI de Riesgo de Viento (kpi_wind_risk)
mide la inestabilidad de la atmósfera basada en la Desviación típica del viento zonal

### KPI de Frecuencia de Eventos Extremos (kpi_extreme_events)
Número de eventos extremos registrados en los últimos 15 días, definidos como días donde tanto la temperatura del mar superó el umbral crítico como el viento máximo superó su umbral crítico. Este KPI proporcionará una medida integrada del riesgo combinado de temperatura y viento.

### KPI de Alerta Temprana (kpi_early_warning) 
Combina los indicadores de temperatura del día y viento para proporcionar una señal de alerta temprana cuando se detecten condiciones que históricamente han precedido a eventos de El Niño, permitiendo a las empresas tomar medidas preventivas con mayor anticipación

---

## Insights principales

Insights clave:
- El análisis de los KPIs revela que el riesgo de eventos extremos (KPI 3) es significativo
- El KPI de Alerta Temprana (KPI 4) demuestra ser un indicador valioso 
- La visualización de los KPIs confirma la relación de causa y efecto entre el comportamiento del viento y la temperatura del mar
---

## Dashboard Tableau

El dashboard incluye:

- Relación entre Temperatura de Mar y Viento Máximo
- Análisis  KPI Alerta Temprana: Dinámica Cruzada Viento-Temperatura
- KPI Eventos Extremos: Número de Eventos Extremos en el Histórico Global
- KPIs Alerta por Temperatura Elevada VS Eventos Extremos
- KPI Alerta por Intensidad del Viento 
- Cronología del Riesgo: Días Reales con Activación de KPIs por Mes

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

La visualización de los KPIs confirma la relación de causa y efecto entre el comportamiento del viento y la temperatura del mar, validando la utilidad de nuestro análisis para monitorear eventos de El Niño y gestionar los riesgos asociados de manera proactiva.

Observamos que un cambio en el rumbo del viento conduce a la elevación de la temperatura del mar, la cual a su vez esta correlacionada con al aumento del Riesgo de Eventos Extremos o sea eventos del Niño

---

## Próximos pasos

- Modelos predictivos
- Otras pistas de anális que especies marínas son las más afectadas por estos eventos

---
