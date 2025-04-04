
import json
import joblib
import numpy as np
import pandas as pd
import os
import traceback
from azureml.core.model import Model

def init():
    global model
    try:
        # Imprimimos información para depuración
        print("Python version:", os.sys.version)
        print("Current working directory:", os.getcwd())
        
        # Obtener la ruta del modelo
        model_path = Model.get_model_path('bankruptcy_model_2nd')
        print(f"Ruta del modelo: {model_path}")
        
        # Verificar si el archivo existe
        if not os.path.exists(model_path):
            print(f"ERROR: El archivo del modelo no existe en {model_path}")
            raise FileNotFoundError(f"No se encuentra el modelo en {model_path}")
            
        # Cargar el modelo
        print("Cargando el modelo...")
        model = joblib.load(model_path)
        print(f"Modelo cargado exitosamente. Tipo: {type(model)}")
        
    except Exception as e:
        print(f"ERROR en init(): {str(e)}")
        print("Traceback completo:")
        traceback.print_exc()
        # Re-lanzar la excepción para que Azure ML pueda registrarla
        raise

def run(raw_data):
    try:
        # Parsear los datos JSON recibidos
        print("Recibiendo datos...")
        data = json.loads(raw_data)['data'][0]
        
        # Convertir a DataFrame
        print("Convirtiendo a DataFrame...")
        data = pd.DataFrame(data)
        print(f"Datos recibidos con forma: {data.shape}")
        
        # Realizar la predicción
        print("Realizando predicción...")
        result_proba = model.predict_proba(data)[:, 1].tolist()  # Probabilidad de clase positiva
        umbral = 0.5500000000000002
        result_finals = [1 if x > umbral else 0 for x in result_proba]
        
        print(f"Predicción completada. Resultados: {result_finals}")
        return json.dumps(result_finals)
    except Exception as e:
        error_message = str(e)
        print(f"ERROR en run(): {error_message}")
        print("Traceback completo:")
        traceback.print_exc()
        return json.dumps({"error": error_message, "traceback": traceback.format_exc()})
