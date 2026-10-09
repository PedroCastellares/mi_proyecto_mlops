# LINEA 1 y 2: Importamos Pandas y la función de entrenamiento de IA que vamos a auditar.
import pandas as pd
from src.modeling import entrenar_modelo_casas

def test_entrenar_modelo_retorna_objeto_valido():
    """
    Prueba automatizada para verificar que el modelo matemático se genera correctamente.
    """
    
    # 1. PREPARACIÓN (Materia prima sintética para la prueba)
    datos_prueba = {
        "habitaciones": [1, 2, 3],
        "precio_real": [100000, 150000, 200000]
    }
    df_prueba = pd.DataFrame(datos_prueba)
    
    # 2. EJECUCIÓN: Le pasamos la tabla a nuestra función de modelado
    modelo_entrenado = entrenar_modelo_casas(df_prueba)
    
    # 3. VALIDACIÓN (Asserts):
    # Afirmamos que el resultado no debe ser vacío (None)
    assert modelo_entrenado is not None, "El modelo regresó un objeto vacío"
    
    # Afirmamos que el objeto tiene el método '.predict' (característica obligatoria de Scikit-Learn)
    # Esto asegura que el modelo está listo para realizar predicciones de precios en producción
    assert hasattr(modelo_entrenado, "predict"), "El objeto devuelto no es un modelo predictivo válido de Scikit-Learn"
