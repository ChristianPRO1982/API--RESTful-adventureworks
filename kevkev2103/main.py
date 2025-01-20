from fastapi import FastAPI
from sqlmodel import Session, select
from database import engine
from models import  Product, SalesOrderHeader, SalesOrderDetail

app = FastAPI()

@app.on_event("startup")
def test_database_connection():
    """Test de la connexion à la base de données et lecture des données."""
    try:
        with Session(engine) as session:
            # Exemple : Vérifier les clients
            products = session.exec(select(Product)).all()
            print(f"Nombre de produits trouvés : {len(products)}")
            print(products[:5])  # Affiche les 5 premiers clients pour vérifier
    except Exception as e:
        print("Erreur lors de la connexion à la base de données :", e)

@app.get("/")
def root():
    return {"message": "API CRUD est opérationnelle !"}
    """Test de la connexion à la base de données et lecture des données."""