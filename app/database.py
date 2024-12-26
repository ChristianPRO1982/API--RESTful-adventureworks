from urllib.parse import quote_plus
from sqlalchemy import create_engine
import os
from app.logs import logging_msg



####################################################################################################
####################################################################################################
####################################################################################################

##################
### CONNECTION ###
##################
def connect()->create_engine:
    log_prefix = '[database | connect]'
    try:
        logging_msg(f"{log_prefix} init env variables", 'DEBUG')

        DRIVER = os.getenv("DRIVER")
        SERVER = os.getenv("SERVER")
        if SERVER.startswith("tcp:"):  # Nettoyage de l'adresse serveur
            SERVER = SERVER.replace("tcp:", "")
        print(SERVER)
        DATABASE = os.getenv("DATABASE")
        UID = os.getenv("UID")
        PWD = os.getenv("PWD")
        ENCRYPT = os.getenv("ENCRYPT")
        TRUSTSERVERCERTIFICATE = os.getenv("TRUSTSERVERCERTIFICATE")
        CONNECTION_TIMEOUT = os.getenv("CONNECTION_TIMEOUT")

        if not all([DRIVER, SERVER, DATABASE, UID, PWD]):
            raise ValueError("Missing required environment variables")
        
        logging_msg(f"{log_prefix} create connection string", 'DEBUG')
        connection_string = (
            f"mssql+pyodbc://{quote_plus(UID)}:{quote_plus(PWD)}@{SERVER},{1433}/{DATABASE}"
            f"?driver={quote_plus(DRIVER)}&encrypt={ENCRYPT}&TrustServerCertificate={TRUSTSERVERCERTIFICATE}"
            f"&timeout={CONNECTION_TIMEOUT}"
        )

        logging_msg(f"{log_prefix} create engine")
        engine = create_engine(connection_string)

        # with engine.connect() as conn:
        #     conn.execute("SELECT 1")

        return engine
    
    except Exception as e:
        logging_msg(f"{log_prefix} Error: {e}", 'CRITICAL')
        return None
    

##################
### DISCONNECT ###
##################
def disconnect(engine:create_engine)->None:
    log_prefix = '[database | disconnect]'
    try:
        logging_msg(f"{log_prefix} close engine")
        engine.dispose()
    
    except Exception as e:
        logging_msg(f"{log_prefix} Error: {e}", 'ERROR')
        return None


####################################################################################################
####################################################################################################
####################################################################################################
