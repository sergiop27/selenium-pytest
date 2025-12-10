from pathlib import Path
import json

def load_login_data():
    """
    Carga el archivo login_data.json y devuelve un diccionario con los datos.
    """
    file_path = Path(__file__).with_name("login_data.json")
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)