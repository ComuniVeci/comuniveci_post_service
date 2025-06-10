import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Cargar las variables desde el archivo .env
load_dotenv()

def get_db():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    db_name = os.getenv("DB_NAME", "communiveci")

    client = MongoClient(mongo_uri)
    return client[db_name]