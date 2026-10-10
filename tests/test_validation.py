import pandas as pd
# Importamos la función de auditoría que acabamos de crear
from src.validation import validar_datos_entrada

def test_validation_datos_correctos_retorna_true():
    """Verifica que el validador apruebe un DataFrame con datos lógicos."""
    datos_buenos = {
        "habitaciones": [1, 2, 3],
        "precio_real": [120000, 150000, 180000]
    }
    df_bueno = pd.DataFrame(datos_buenos)
    
    # Afirmamos que el resultado obligatorio debe ser True
    assert validar_datos_entrada(df_bueno) is True


def test_validation_datos_corruptos_retorna_false():
    """Verifica que el validador repruebe un DataFrame con habitaciones incoherentes."""
    datos_malos = {
        "habitaciones": [3, -1, 4],  # Metemos un -1 a propósito
        "precio_real": [150000, 100000, 180000]
    }
    df_malo = pd.DataFrame(datos_malos)
    
    # Afirmamos que el resultado obligatorio debe ser False
    assert validar_datos_entrada(df_malo) is False
