import os
from dotenv import load_dotenv
load_dotenv()
    
PORT_API = int(os.environ.get("PORT_API"))
RELOAD = os.environ.get("RELOAD", "False").lower()
HOST_API = os.environ.get("HOST_API", "localhost")
API_VERSION = os.environ.get("API_VERSION")