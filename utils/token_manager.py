from jwt import encode, decode
from dotenv import load_dotenv
import os
import secrets

load_dotenv()

def login(username, password):
    if username == os.getenv("USERNAME") and password == os.getenv("PASSWORD"):
        return create_api_key()
    else:
        return False

def create_api_key():
    api_key = secrets.token_urlsafe(32)

    # Save the api_key to the .env file
    with open(".env", "a") as f:
        f.write(f"\nAPI_KEY={api_key}")

    return api_key



def validate_api_key(api_key):
    return api_key == os.getenv("API_KEY")
    
