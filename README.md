# ACTIVIDAD-4
ACTIVIDAD DE COMPARACIÓN DE MODELOS
# Benchmark de Modelos Preentrenados de Hugging Face (NLP)

Este repositorio contiene la implementación, evaluación comparativa y documentación técnica para la clasificación automática de reportes de mantenimiento industrial e incidencias de TI utilizando modelos Transformer preentrenados de Hugging Face.

# Descripción del Proyecto
El objetivo del prototipo es evaluar y seleccionar el modelo más eficiente para el enrutamiento automático de tickets operativos. Se compararon tres arquitecturas (`bert-base-multilingual-cased`, `roberta-base` y `distilbert-base-uncased`) bajo métricas estándar (`Accuracy`, `Precision`, `Recall`, `F1-Score`) y latencia de inferencia en milisegundos.

---

# Entorno de Ejecución
* **Plataforma:** Google Colab
* **Aceleración por Hardware:** GPU (NVIDIA A100 / T4)
* **Lenguaje:** Python 3.10+
* **Librerías Clave:** `transformers`, `datasets`, `torch`, `scikit-learn`

---

# Pasos para la Ejecución y Reproducibilidad

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/rserenadlc/ACTIVIDAD-4.git](https://github.com/rserenadlc/ACTIVIDAD-4.git)
   cd huggingface-model-benchmark
