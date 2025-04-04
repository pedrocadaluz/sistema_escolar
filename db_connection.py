from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database_name = os.getenv("DB_NAME")

if not all([host, port, user, password, database_name]):
    raise ValueError("Variáveis de ambiente do banco não foram corretamente carregadas.")

DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database_name}"

def get_engine():
    return create_engine(DATABASE_URL)
