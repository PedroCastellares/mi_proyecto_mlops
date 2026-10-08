# LINEA 1: Importamos la librería Pandas. 
# Le ponemos el apodo 'pd' para escribir menos código cuando llamemos a sus funciones.
import pandas as pd

# LINEA 4: Definimos nuestra función (nuestra "máquina").
# No requiere que le pasemos ningún dato inicial entre los paréntesis para arrancar.
def cargar_datos_casas():
    """
    Simula la ingesta de datos de un lote de casas para el modelo.
    """
    
    # LINEA 11: Mostramos un mensaje informativo en la terminal.
    # En MLOps esto ayuda a saber en qué etapa va el sistema si algo se congela.
    print("📥 Iniciando la ingesta de datos...")
    
    # LINEA 15: Creamos un diccionario (una estructura de datos clave:valor).
    # Aquí agregamos los números reales que faltaban dentro de las listas [].
    datos_crudos = {
        "habitaciones":[1, 2, 3, 4, 5],
        "precio_real": [115000, 130000, 145000, 160000, 175000]
    }
    
    # LINEA 22: Usamos Pandas para transformar el diccionario en un 'DataFrame'.
    # Un DataFrame es, literalmente, una tabla estructurada con filas y columnas (como un Excel en memoria).
    df_casas = pd.DataFrame(datos_crudos)
    
    # LINEA 26: Medimos la longitud de la tabla usando 'len()' para confirmar cuántas filas cargamos.
    # Usamos un f-string para inyectar ese número dinámicamente en el mensaje.
    print(f"✅ Ingesta completada. Se cargaron {len(df_casas)} registros.")
    
    # LINEA 30: Devolvemos la tabla de Pandas como el "producto terminado".
    # Cualquier otro archivo que llame a esta función recibirá esta tabla lista para usarse.
    return df_casas
