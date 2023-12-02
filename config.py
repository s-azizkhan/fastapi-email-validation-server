from dotenv import load_dotenv
from os import getenv 

load_dotenv()

# Set the port number for the API
PORT = int(getenv("PORT", 8000))

# Set the environment for the API
ENVIRONMENT = getenv("ENVIRONMENT", "development")

# Set the prefix for the API endpoints
API_PREFIX = getenv("API_PREFIX", "/api")

# Set the secret key for the API
API_SECRET_KEY = getenv("API_SECRET_KEY", range(16, 32, 3))
