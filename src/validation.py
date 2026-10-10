# Importamos Pandas para poder analizar la estructura de la tabla de datos
import pandas as pd

def validar_datos_entrada(df):
    """Audita el DataFrame para detectar anomalías o errores silenciosos.

    Args:
        df (pd.DataFrame): Tabla de datos extraída por el módulo de ingesta.

    Returns:
        bool: True si los datos son perfectos para entrenar, False si están corruptos.
    """
    print("\n🔍 [Validación] Iniciando la auditoría de calidad de datos...")
    
    # 1. CONTROL DE VALORES NULOS (Datos vacíos)
    # '.isnull().sum().sum()' cuenta cuántas celdas vacías hay en toda la tabla
    total_nulos = df.isnull().sum().sum()
    if total_nulos > 0:
        print(f"❌ [ERROR CRÍTICO] Se encontraron {total_nulos} valores vacíos (nulos) en el dataset.")
        return False
        
    # 2. CONTROL DE VALORES COHERENTES (Lógica del negocio)
    # Verificamos si hay alguna fila donde las habitaciones sean menores o iguales a cero
    # '.any()' devuelve True si al menos un registro cumple con esa condición errónea
    if (df["habitaciones"] <= 0).any():
        print("❌ [ERROR CRÍTICO] Se detectaron registros con 0 o menos habitaciones. Datos incoherentes.")
        return False
        
    # 3. CONTROL DE PRECIOS NEGATIVOS
    if (df["precio_real"] <= 0).any():
        print("❌ [ERROR CRÍTICO] Se detectaron propiedades con precios menores o iguales a cero.")
        return False

    # Si los datos superan con éxito las 3 auditorías, el portero da luz verde
    print("✅ [Validación] Datos validados con éxito. Calidad 100% óptima para la IA.")
    return True
