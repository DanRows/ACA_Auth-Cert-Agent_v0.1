@echo off
setlocal enabledelayedexpansion

:: Crear directorios principales
mkdir aca-certification
cd aca-certification
mkdir scripts docs tests src logs
mkdir src\config src\api src\services src\utils src\workflows
mkdir src\api\routes src\api\models

:: Crear archivos raíz
type nul > README.md
type nul > .env.example
type nul > .gitignore
type nul > pyproject.toml
type nul > docker-compose.yml
type nul > Dockerfile
type nul > requirements.txt
type nul > Makefile

:: Crear archivos en scripts
cd scripts
type nul > __init__.py
type nul > setup.sh
type nul > test.sh
cd ..

:: Crear archivos en docs
cd docs
type nul > api.md
type nul > setup.md
type nul > architecture.md
cd ..

:: Crear archivos en tests
cd tests
type nul > __init__.py
type nul > conftest.py
type nul > test_api.py
type nul > test_services.py
type nul > test_utils.py
cd ..

:: Crear archivos en src y subdirectorios
cd src
type nul > __init__.py

cd config
type nul > __init__.py
type nul > settings.py
cd ..

cd api
type nul > __init__.py
type nul > dependencies.py

cd routes
type nul > __init__.py
type nul > certificates.py
type nul > documents.py
type nul > support.py
cd ..

cd models
type nul > __init__.py
type nul > certificate.py
type nul > document.py
type nul > support.py
cd ..
cd ..

cd services
type nul > __init__.py
type nul > sambanova.py
type nul > certificate_service.py
type nul > document_service.py
type nul > support_service.py
cd ..

cd utils
type nul > __init__.py
type nul > validators.py
type nul > helpers.py
cd ..

cd workflows
type nul > __init__.py
type nul > n8n_flows.json
cd ..
cd ..

:: Crear .gitkeep en logs
cd logs
type nul > .gitkeep
cd ..

echo Estructura del proyecto creada exitosamente!