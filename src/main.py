import os
import sys

# Aseguramos que Python encuentre las rutas locales de la carpeta 'src'
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Importamos las dos funciones de nuestros módulos independientes
from ingestion import cargar_datos_casas
from modeling import entrenar_modelo_casas

print("🚀 === INICIANDO PIPELINE END-TO-END DE MLOps ===")

# ETAPA 1: Ingestión de datos
datos_crudos = cargar_datos_casas()

# ETAPA 2: Entrenamiento del modelo
modelo_final = entrenar_modelo_casas(datos_crudos)

print("\n🚀 === PIPELINE EJECUTADO CON ÉXITO ===")

