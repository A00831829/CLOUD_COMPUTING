# CLOUD_COMPUTING

Repositorio para el desarrollo.

## Requisitos

- Python 3.10
- [uv](https://github.com/astral-sh/uv) (gestor de entornos y dependencias ultrarrápido)

## Instalación

### 1. Clonar el repositorio

>> git clone https://github.com/A00831829/CLOUD_COMPUTING.git
>> cd CLOUD_COMPUTING

### 2. Crear un entorno e implementar libreías

>> uv venv
>> uv pip install -r requirements.txt

### 3. Activar el entorno

Para Windows
>> .\.venv\Scripts\activate
Para macOS / Linux
>> source .venv/bin/activate

### 5. Obtener el modelo

Correr el archivo 'modelo.ipynb' para generar el modelo

### 4. Añadir archivos 'id_CONFIDENTIAL.json'

El usuario debe añadir su popía llave confidencial de su ID de Azure.
Añadir a los archivos en un '.json' con el siguiente formato:
----------
{
    "my_id": "PEGA AQUI TU ID"
}
----------

### 5. Correr el deployer para subir el modelo a Azure

Correr el archivo 'deployer.ipynb'

### 6. Probar el modelo

Correr el archivo 'api.ipynb'

### 7. Listo!!!
