# LINEA 1: Descargamos una imagen oficial de Linux ligera que ya viene con Python 3.12 preinstalado.
FROM python:3.12-slim

# LINEA 4: Creamos y nos mudamos a una carpeta interna dentro del contenedor llamada '/app'.
# Todo nuestro proyecto vivirá guardado allí adentro.
WORKDIR /app

# LINEA 8: Copiamos tu archivo de "receta" desde tu laptop hacia el interior del contenedor.
COPY requirements.txt .

# LINEA 12: Desactivamos el bloqueo de archivos de MLflow dentro del entorno del contenedor.
ENV MLFLOW_ALLOW_FILE_STORE=true

# LINEA 15: Le ordenamos a la máquina Linux que instale todas las librerías de tu receta.
RUN pip install --no-cache-dir -r requirements.txt

# LINEA 18: Copiamos todo el resto de tus carpetas locales (src, data, tests, pytest.ini) al contenedor.
COPY . .

# Modificamos la línea final para levantar el servidor web dentro de la cápsula
CMD ["mlflow", "server", "--backend-store-uri", "./mlruns", "--host", "0.0.0.0", "--port", "5000"]
