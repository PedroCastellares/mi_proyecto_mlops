import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Importamos las funciones de nuestros tres módulos independientes
from ingestion import cargar_datos_casas
from validation import validar_datos_entrada
from modeling import entrenar_modelo_casas
import mlflow

def ejecutar_pipeline_completo():
    print("🚀 === INICIANDO PIPELINE END-TO-END DE MLOps ===")

    # ETAPA 1: Ingestión de datos
    datos_crudos = cargar_datos_casas()

    # ETAPA 2: Validación de calidad de datos (El Escudo)
    # Llamamos al validador y evaluamos su respuesta booleana
    if not validar_datos_entrada(datos_crudos):
        print("\n🛑 [PIPELINE ABORTADO] Los datos están corruptos. Entrenamiento cancelado para proteger la IA.")
        return None

    # ETAPA 3: Entrenamiento del modelo (Solo ocurre si la validación da True)
    modelo_final = entrenar_modelo_casas(datos_crudos)

    # ETAPA 4: Consulta automática de la bitácora
    print("\n📊 === CONSULTANDO EL CUADERNO DE EXPERIMENTOS EN VIVO ===")
    runs = mlflow.search_runs()
    
    print("\n-------------------------------------------------------------")
    print(" NOMBRE DEL RUN              | PARÁMETRO (Intercept) | MÉTRICA (R²)")
    print("-------------------------------------------------------------")
    for _, fila in runs.iterrows():
        nombre = fila["tags.mlflow.runName"]
        parametro = fila["params.fit_intercept"]
        metrica = fila["metrics.r2_score"]
        print(f" {nombre:<26} | {parametro:<21} | {metrica:.2f}")
    print("-------------------------------------------------------------")
    
    print("🚀 === PIPELINE EJECUTADO CON ÉXITO ===")


if __name__ == "__main__":
    os.environ["MLFLOW_ALLOW_FILE_STORE"] = "true"
    ejecutar_pipeline_completo()
