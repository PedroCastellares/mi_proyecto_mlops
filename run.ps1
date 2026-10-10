# 🛠️ CONTROL REMOTO NATIVO DE AUTOMATIZACIÓN PARA WINDOWS

function Run-Test {
    write-host "🧪 Ejecutando pruebas unitarias de calidad..." -ForegroundColor Cyan
    pytest
}

function Run-Build {
    write-host "🐳 Construyendo la imagen de Docker aislada..." -ForegroundColor Cyan
    docker build -t mi_pipeline_mlops .
}

function Run-Pipeline {
    write-host "🚀 Corriendo el pipeline de IA blindado dentro de Docker..." -ForegroundColor Cyan
    docker run --rm mi_pipeline_mlops sh -c "python src/main.py"
}

# Ejecutamos las tres tareas en orden automático como un pipeline real
Run-Test
if ($LASTEXITCODE -eq 0) {
    Run-Build
    Run-Pipeline
} else {
    write-host "🛑 Pruebas fallidas. El pipeline se detuvo por seguridad." -ForegroundColor Red
}
