from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import init_db
from datetime import datetime
from app.logs import logging_msg
from app.database import init_db
from app import crud, models



app = FastAPI()

####################################################################################################
####################################################################################################
####################################################################################################

###############
### STARTUP ###
###############

# @app.on_event("startup")
# def on_startup():
#     init_db()


##############
### GET DB ###
##############

def get_db():
    db = init_db()
    try:
        yield db
    finally:
        db.close()


####################################################################################################
####################################################################################################
####################################################################################################

############
### ROOT ###
############

@app.get("/")
def read_root():
    return "[" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "] Welcome to FastAPI project! All informations are available on /docs"


################
### PRODUCTS ###
################

@app.get("/products/")
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db=db, skip=skip, limit=limit)
