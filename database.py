import pymongo
from werkzeug.security import generate_password_hash
import os
import sys

def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

# Configuración de MongoDB
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.environ.get("MONGO_DB_NAME", "soporte_draj")

# Leer IP desde config.txt si existe y NO hay variable de entorno
if "MONGO_URI" not in os.environ:
    config_path = os.path.join(get_base_path(), 'config.txt')
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            ip = f.read().strip()
            if ip:
                MONGO_URI = f"mongodb://{ip}:27017/"

def get_db_connection():
    """
    Retorna la conexión a la base de datos de MongoDB.
    """
    client = pymongo.MongoClient(MONGO_URI)
    return client[DB_NAME]

def init_db():
    db = get_db_connection()
    
    # Crear usuario por defecto si no existe
    if not db.usuarios.find_one({"username": "admin"}):
        hashed_pw = generate_password_hash('admin123')
        db.usuarios.insert_one({
            "username": "admin",
            "password": hashed_pw,
            "nombre": "Administrador TI"
        })

if __name__ == '__main__':
    init_db()
    print("Base de datos MongoDB conectada e inicializada correctamente.")
