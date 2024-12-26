from urllib.parse import quote_plus
from sqlalchemy import create_engine
import dotenv
import os
from logs import init_log, logging_msg



####################################################################################################
####################################################################################################
####################################################################################################

############
### INIT ###
############
def init()->bool:
    log_prefix = '[database | init]'
    try:
        init_log()
        dotenv.load_dotenv('.env', override=True)

        logging_msg(f"{log_prefix} OK")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False


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

############
### MAIN ###
############
if __name__ == "__main__":
    log_prefix = '[database | main]'
    try:
        if init():
            engine = connect()
            logging_msg("OOKK", 'WARNING')
            disconnect(engine)
            
    
    except Exception as e:
        logging_msg(f"{log_prefix} Error: {e}", 'CRITICAL')