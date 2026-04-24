# 🚀 Proyecto ETL SpaceX

Pipeline ETL que extrae datos de la API de SpaceX, los almacena en Supabase y los visualiza con Streamlit.

## 🧱 Tecnologías
- Python
- Pandas
- Streamlit
- Supabase (PostgreSQL)
- SQLAlchemy

## 🔄 Flujo ETL
1. Extracción desde API SpaceX
2. Transformación con Pandas
3. Carga en Supabase

## 📊 Dashboard
Visualización interactiva con:
- KPIs de lanzamientos
- Gráficos de éxito vs fallo
- Lanzamientos por año
- Filtros dinámicos

## 🌐 App en producción
[PEGAR TU LINK DE STREAMLIT AQUÍ]

## ⚙️ Cómo ejecutar localmente

```bash
pip install -r requirements.txt
streamlit run dashboard_spacex.py