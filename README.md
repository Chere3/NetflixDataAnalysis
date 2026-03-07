
# Análisis de Datos de Contenido de Netflix

Este repositorio contiene un análisis exploratorio completo del catálogo de contenido de Netflix, enfocándose en películas, series y otros tipos de contenido disponibles en la plataforma. El proyecto examina patrones de distribución, características temporales y geográficas del contenido a través de un dataset con 4,812 registros.

## Descripción del Proyecto

El análisis se centra en comprender la composición del catálogo de Netflix, evaluando la distribución de contenido por tipo, país de origen, géneros, años de lanzamiento y fechas de incorporación a la plataforma. Los datos proporcionan insights sobre las estrategias de contenido y preferencias de la plataforma.

## Estructura del Análisis

### 1. Exploración de Datos
- Carga y examen inicial del dataset de Netflix
- Análisis de estructura y completitud de datos
- Identificación de tipos de variables y características generales
- Estadísticas descriptivas del catálogo

### 2. Preprocesamiento
- Validación de integridad de datos (sin valores faltantes detectados)
- Procesamiento de variables temporales (fechas de lanzamiento y agregación)
- Extracción de componentes de fecha (año, mes, día)
- Preparación de variables categóricas para análisis

### 3. Modelado
- Análisis de distribución temporal del contenido
- Segmentación por tipo de contenido (películas vs series)
- Análisis geográfico de producción de contenido
- Evaluación de patrones de géneros y categorías

### 4. Resultados
- Identificación de sesgo hacia películas en el catálogo
- Dominancia de Estados Unidos en producción de contenido
- Patrones temporales de incorporación de contenido
- Distribución de géneros y categorías principales

### 5. Reporte
- Insights sobre estrategia de contenido de Netflix
- Análisis de diversidad geográfica y temporal
- Recomendaciones para análisis posteriores
- Identificación de oportunidades de investigación adicional

## Dataset

El dataset contiene 11 columnas principales:
- **Identificación**: show_id, title, type
- **Metadatos de producción**: director, cast, country, release_year
- **Información de plataforma**: date_added, duration
- **Contenido**: description, genre

## Hallazgos Principales

- **Distribución de contenido**: Sesgo significativo hacia películas sobre series
- **Producción geográfica**: Estados Unidos lidera la producción de contenido
- **Calidad de datos**: Dataset completo sin valores faltantes
- **Diversidad temporal**: Amplio rango de años de lanzamiento y fechas de incorporación

## Entorno Reproducible

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/validate_dataset.py
python scripts/generate_quality_report.py
```

## Flujo de ejecución recomendado
1. `notebooks/netflix/01_exploracion.ipynb`
2. `notebooks/netflix/02_preprocesamiento.ipynb`
3. `notebooks/netflix/03_modelado.ipynb`
4. `notebooks/netflix/04_resultados.ipynb`
5. `notebooks/netflix/05_reporte.ipynb`

## Calidad y automatización
- Se incluye un validador de calidad de datos en `scripts/validate_dataset.py`
- Se genera un reporte de calidad en Markdown con `scripts/generate_quality_report.py`
- CI ejecuta validación automática en PRs y pushes a `dev`
- CI publica artefacto `netflix-data-quality-report` en cada ejecución
- Roadmap estratégico: [ROADMAP.md](./ROADMAP.md)

## Tecnologías Utilizadas

- **Python** - Lenguaje principal de análisis
- **Pandas** - Manipulación y análisis de datos
- **Matplotlib & Seaborn** - Visualización de datos
- **Jupyter Notebook** - Entorno de desarrollo interactivo

## Próximos Pasos

El análisis sugiere la necesidad de segmentación adicional por categorías específicas, géneros y duraciones para análisis más profundos y potencial modelado predictivo del contenido de Netflix.