from fastapi import FastAPI
from app.logs import logging_msg
from .database import init_db


app = FastAPI()

####################################################################################################
####################################################################################################
####################################################################################################

###############
### STARTUP ###
###############

@app.on_event("startup")
def on_startup():
    init_db()

############
### ROOT ###
############

@app.get("/")
def read_root():
    return "Welcome to FastAPI project! All informations are available on /docs"
