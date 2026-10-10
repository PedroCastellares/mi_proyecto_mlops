# 🛠️ CONTROL REMOTO DE AUTOMATIZACIÓN DE MLOPS

.PHONY: test build run clean

# Tarea 1: Ejecutar las pruebas unitarias locales
test:
	pytest

# Tarea 2: Construir la imagen de Docker limpia
build:
	docker build -t mi_pipeline_mlops .

# Tarea 3: Correr el pipeline de IA blindado dentro del contenedor
run:
	docker run --rm mi_pipeline_mlops sh -c "python src/main.py"

# Tarea 4: Limpiar archivos temporales de la caché de Python
clean:
	rm -rf src/__pycache__ tests/__pycache__ .pytest_cache
