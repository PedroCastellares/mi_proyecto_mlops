# LINEA 1 y 2: Importamos Pandas y la función real que queremos poner a prueba.
import pandas as pd
from src.ingestion import cargar_datos_casas

# LINEA 5: Definimos la función de prueba. 
# También DEBE empezar con el prefijo 'test_'.
def test_cargar_datos_casas_retorna_dataframe_valido():
    """
    Prueba automatizada para verificar que la ingesta funciona correctamente.
    """
    
    # 1. EJECUCIÓN: Llamamos a la función real para ver qué nos devuelve.
    resultado_df = cargar_datos_casas()
    
    # 2. VALIDACIÓN (Asserts): Usamos la palabra 'assert' (afirmar).
    # Le decimos a Python: "Yo afirmo que esto debe ser VERDADERO. Si no lo es, rompe el test".
    
    # Afirmamos que el resultado debe ser un DataFrame de Pandas (una tabla)
    assert isinstance(resultado_df, pd.DataFrame), "El resultado no es un DataFrame de Pandas"
    
    # Afirmamos que la tabla debe tener exactamente 5 filas
    assert len(resultado_df) == 5, f"Se esperaban 5 filas, pero se obtuvieron {len(resultado_df)}"
    
    # Afirmamos que la columna 'precio_real' debe existir dentro de la tabla
    assert "precio_real" in resultado_df.columns, "La columna 'precio_real' no se encuentra en el DataFrame"
