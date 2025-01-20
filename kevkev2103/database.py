# create_engine: sert à configurer la connexion à la base de données
# SQLModel: utilisé pour gérer les modèles et les tables (interaction avec les données)
#Session : permet l'exécution des requêtes SQL

from sqlmodel import create_engine, SQLModel, Session

#dotenv permet de charger les variables d'env depuis un fichier .env
#os : fournit un moyen d'accéder aux variables d'env du système

from dotenv import load_dotenv
import os

#charger les V.E depuis .env
load_dotenv()


# Récupérer DATABASE_URL depuis .env
DATABASE_URL = os.getenv("DATABASE_URL")

#Configurer le moteur de la base de données
engine = create_engine(DATABASE_URL, echo=True)


# def test_connection():
#     try:
#         SQLModel.metadata.create_all(engine)
#         print("Connexion réussie à la base de données !")
#     except Exception as e:
#         print("Erreur de connexion :", e)


# if __name__ =="__main__":
#     test_connection()


def get_session():
    with Session(engine) as session:
        yield session