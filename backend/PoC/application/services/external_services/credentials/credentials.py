import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY") 
#API_KEY = os.environ['API_KEY']
ACCESS_TOKEN = (
    API_KEY
)
