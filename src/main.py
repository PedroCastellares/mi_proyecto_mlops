import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from ingestion import cargar_datos_casas
from modeling import entrenar_modelo_casas
# Importamos la herramienta de búsqueda de MLflow
import mlflow

def ejecutar_pipeline_completo():
    print("🚀 === INICIANDO PIPELINE END-TO-END DE MLOps ===")

    # ETAPA 1: Ingestión de datos
    datos_crudos = cargar_datos_casas()

    # ETAPA 2: Entrenamiento de múltiples modelos
    modelo_final = entrenar_modelo_casas(datos_crudos)

    # ETAPA 3: Lectura automática de la bitácora (El reemplazo del Navegador Web)
    print("\n📊 === CONSULTANDO EL CUADERNO DE EXPERIMENTOS EN VIVO ===")
    
    # Buscamos de forma automática todos los registros guardados en la bitácora
    runs = mlflow.search_runs()
    
    print("\n-------------------------------------------------------------")
    print(" NOMBRE DEL RUN              | PARÁMETRO (Intercept) | MÉTRICA (R²)")
    print("-------------------------------------------------------------")
    
    # Recorremos la bitácora y la imprimimos limpia en la consola
    for _, fila in runs.iterrows():
        nombre = fila["tags.mlflow.runName"]
        parametro = fila["params.fit_intercept"]
        metrica = fila["metrics.r2_score"]
        print(f" {nombre:<26} | {parametro:<21} | {metrica:.2f}")
        
    print("-------------------------------------------------------------")
    print("🚀 === PIPELINE EJECUTADO CON ÉXITO ===")


if __name__ == "__main__":
    # Inyectamos la llave de escape directo en el código para que nunca falle por el Maintenance Mode
    os.environ["MLFLOW_ALLOW_FILE_STORE"] = "true"
    ejecutar_pipeline_completo()
