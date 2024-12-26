from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

# Récupérer les informations de connexion
db_server = os.getenv("DB_SERVER")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# Construire l'URL de connexion
DATABASE_URL = f"mssql+pyodbc://{db_user}:{db_password}@{db_server}/{db_name}?driver=ODBC+Driver+18+for+SQL+Server"

# Créer le moteur SQLAlchemy
engine = create_engine(DATABASE_URL)

# Lire les données de la table
try:
    query = "SELECT TOP 5 * FROM AWBuildVersion"
    with engine.connect() as connection:
        df = pd.read_sql(query, connection)
        print("Premières lignes de la table AWBuildVersion :")
        print(df)
except Exception as e:
    print("Erreur lors de la lecture des données :", e)
