# LINEA 1: Importamos la librería Pandas para manipular tablas de datos.
import pandas as pd

def cargar_datos_casas():
    """Simula la ingesta de datos leyendo un archivo CSV real custodiado por DVC.

    Returns:
        pd.DataFrame: Tabla estructurada con los datos cargados desde el archivo.
    """
    # LINEA 10: Definimos la ruta exacta donde vive nuestro dataset físico.
    # El archivo fue creado en la carpeta 'data/' en el Paso 29.
    ruta_dataset = "data/datos_casas.csv"
    
    print(f"📥 Iniciando la ingesta de datos desde: {ruta_dataset}...")
    
    # LINEA 15: Usamos la función nativa de Pandas '.read_csv()' para abrir el archivo.
    # Esta función lee el archivo en disco y lo transforma automáticamente en un DataFrame.
    df_casas = pd.read_csv(ruta_dataset)
    
    # LINEA 19: Medimos la cantidad de filas cargadas usando 'len()'.
    print(f"✅ Ingesta completada. Se cargaron {len(df_casas)} registros desde el CSV.")
    
    # LINEA 22: Devolvemos la tabla lista para ser consumida por el modelo de IA.
    return df_casas
