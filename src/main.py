import os
import sys

# Aseguramos que Python encuentre las rutas locales de la carpeta 'src'
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from ingestion import cargar_datos_casas
from modeling import entrenar_modelo_casas

def ejecutar_pipeline_completo():
    """Ejecuta el pipeline completo de MLOps desde la ingesta hasta el modelo.

    Este orquestador coordina la extracción de los datos simulados y alimenta
    el algoritmo de Regresión Lineal de Scikit-Learn para entrenar la IA.

    Returns:
        LinearRegression: Objeto del modelo entrenado listo para producción.
    """
    print("🚀 === INICIANDO PIPELINE END-TO-END DE MLOps ===")

    # ETAPA 1: Ingestión de datos
    datos_crudos = cargar_datos_casas()

    # ETAPA 2: Entrenamiento del modelo
    modelo_final = entrenar_modelo_casas(datos_crudos)

    print("\n🚀 === PIPELINE EJECUTADO CON ÉXITO ===")
    return modelo_final


# LINEA 31: El bloque de control de ejecución nativo de Python.
if __name__ == "__main__":
    ejecutar_pipeline_completo()
