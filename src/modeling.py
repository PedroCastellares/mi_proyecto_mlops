# LINEA 1: Importamos la clase de Regresión Lineal de Scikit-Learn.
# Esta librería contiene el algoritmo matemático que aprenderá de los datos.
from sklearn.linear_model import LinearRegression

# LINEA 5: Definimos nuestra función de entrenamiento.
# Recibe como "materia prima" la tabla de datos (df) que procesó el archivo de ingesta.
def entrenar_modelo_casas(df):
    """
    Entrena un modelo matemático de Regresión Lineal usando la tabla de datos provista.
    """
    print("\n🤖 Iniciando el entrenamiento del modelo de IA...")
    
    # LINEA 12: Separamos nuestras características (X) de nuestro objetivo a predecir (y).
    # 'X' debe ser una matriz de dos dimensiones, por eso usamos doble corchete [["habitaciones"]].
    X = df[["habitaciones"]]
    y = df["precio_real"]
    
    # LINEA 17: Creamos una instancia limpia del algoritmo (nuestro cerebro artificial vacío).
    modelo = LinearRegression()
    
    # LINEA 20: La magia del Machine Learning ocurre aquí.
    # El método '.fit()' hace que el algoritmo ajuste sus parámetros matemáticos internos 
    # analizando los datos reales de X e y. El modelo queda "entrenado".
    modelo.fit(X, y)
    
    # LINEA 24: Calculamos la precisión del entrenamiento (R² score).
    # Nos da un número entre 0 y 1 para saber qué tan bien entendió el modelo el patrón de los datos.
    precision = modelo.score(X, y)
    print(f"🎯 ¡Modelo entrenado con éxito! Precisión del ajuste (R²): {precision:.2f}")
    
    # LINEA 28: Devolvemos el objeto del modelo entrenado listo para predecir precios en producción.
    return modelo
