from sqlmodel import SQLModel, create_engine
from urllib.parse import quote_plus
import dotenv
import os
from app.logs import init_log, logging_msg



####################################################################################################
####################################################################################################
####################################################################################################

############
### INIT ###
############
def init()->bool:
    log_prefix = '[database | init]'
    try:
        dotenv.load_dotenv('.env', override=True)
        init_log()

        logging_msg(f"{log_prefix} OK")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False

############
### MAIN ###
############

try:
    if init():
        dotenv.load_dotenv('.env', override=True)

        log_prefix = '[database | main]'

        DRIVER = os.getenv("DRIVER")
        SERVER = os.getenv("SERVER")
        if SERVER.startswith("tcp:"):  # Nettoyage de l'adresse serveur
            SERVER = SERVER.replace("tcp:", "")
        DATABASE = os.getenv("DATABASE")
        UID = os.getenv("UID")
        PWD = os.getenv("PWD")
        ENCRYPT = os.getenv("ENCRYPT")
        TRUSTSERVERCERTIFICATE = os.getenv("TRUSTSERVERCERTIFICATE")
        CONNECTION_TIMEOUT = os.getenv("CONNECTION_TIMEOUT")

        if not all([DRIVER, SERVER, DATABASE, UID, PWD]):
            raise ValueError("Missing required environment variables")

        logging_msg(f"{log_prefix} create connection string", 'DEBUG')
        DATABASE_URL = (
            f"mssql+pyodbc://{quote_plus(UID)}:{quote_plus(PWD)}@{SERVER},{1433}/{DATABASE}"
            f"?driver={quote_plus(DRIVER)}&encrypt={ENCRYPT}&TrustServerCertificate={TRUSTSERVERCERTIFICATE}"
            f"&timeout={CONNECTION_TIMEOUT}"
        )

        engine = create_engine(DATABASE_URL, echo=True)

    else:
        raise Exception("Error during init")

except Exception as e:
    print("Critical Error from init database.py: ", e)


####################################################################################################
####################################################################################################
####################################################################################################

#################
### FONCTIONS ###
#################

def init_db():
    SQLModel.metadata.create_all(engine)
