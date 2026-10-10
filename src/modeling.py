from sklearn.linear_model import LinearRegression
import mlflow

def entrenar_modelo_casas(df):
    """Entrena dos versiones del modelo con configuraciones distintas y las trackea en MLflow."""
    X = df[["habitaciones"]]
    y = df["precio_real"]
    
    # 🧪 EXPERIMENTO 1: Modelo Base (Con Intercepto)
    print("\n🤖 [Run 1] Entrenando Modelo Base (fit_intercept=True)...")
    with mlflow.start_run(run_name="Experimento_Base"):
        modelo_1 = LinearRegression(fit_intercept=True)
        modelo_1.fit(X, y)
        precision_1 = modelo_1.score(X, y)
        
        mlflow.log_param("fit_intercept", True)
        mlflow.log_metric("r2_score", precision_1)
        mlflow.sklearn.log_model(modelo_1, artifact_path="modelo_casas")
        print(f"🎯 [Run 1] Completado. Precisión (R²): {precision_1:.2f}")

    # 🧪 EXPERIMENTO 2: Modelo Modificado (Sin Intercepto)
    # Obligamos a la línea matemática a cruzar por el cero absoluto de la gráfica.
    print("\n🤖 [Run 2] Entrenando Modelo Alternativo (fit_intercept=False)...")
    with mlflow.start_run(run_name="Experimento_Sin_Intercepto"):
        modelo_2 = LinearRegression(fit_intercept=False)
        modelo_2.fit(X, y)
        precision_2 = modelo_2.score(X, y)
        
        mlflow.log_param("fit_intercept", False)
        mlflow.log_metric("r2_score", precision_2)
        mlflow.sklearn.log_model(modelo_2, artifact_path="modelo_casas")
        print(f"🎯 [Run 2] Completado. Precisión (R²): {precision_2:.2f}")
        
    return modelo_1

