from fastapi import FastAPI
from app.logs import logging_msg
from .database import init_db
from datetime import datetime


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
    return "[" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "] Welcome to FastAPI project! All informations are available on /docs"
