from sqlmodel import SQLModel, create_engine, Session
from urllib.parse import quote_plus
import dotenv
import os
import subprocess
from app.logs import init_log, logging_msg



# Global engine shared across the app
engine = None  # Déclaré globalement pour être réutilisé

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
    

def generate_secret_key():
    # to get a string like this run:
    # openssl rand -hex 32
    result = subprocess.run(["openssl", "rand", "-hex", "32"], capture_output=True, text=True)
    logging_msg("generate_secret_key():" + result.stdout.strip(), 'DEBUG')
    return result.stdout.strip()


def secrets()->tuple:
    try:
        SECRET_KEY = generate_secret_key()
        ALGORITHM = "HS256"
        ACCESS_TOKEN_EXPIRE_MINUTES = 30

        return SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
    

    except Exception as e:
        print(f"Error: {e}")
        return None, None, None


##############
### ENGINE ###
##############
def main_create_engine()->create_engine:
    log_prefix = '[database | main]'

    try:
        if init():
            dotenv.load_dotenv('.env', override=True)
            
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
            logging_msg(f"{log_prefix} engine created", 'INFO')
            return engine

        else:
            raise Exception("Error during init")

    except Exception as e:
        logging_msg(f"{log_prefix} {e}", 'ERROR')
        return None


####################################################################################################
####################################################################################################
####################################################################################################

#################
### FONCTIONS ###
#################

def init_db()->tuple:
    """Initialise le moteur et les tables."""
    try:
        global engine  # Référence à l'engine global
        if not engine:
            engine = main_create_engine()
        if engine:
            SQLModel.metadata.create_all(engine)
        else:
            raise RuntimeError("Engine is not initialized. Check the logs for errors.")


    except Exception as e:
        print(f"Error: {e}")

def get_session():
    """Retourne une session connectée au moteur."""
    global engine  # Référence à l'engine global
    if not engine:
        engine = main_create_engine()
    if not engine:
        raise RuntimeError("Failed to create engine.")
    return Session(engine)
