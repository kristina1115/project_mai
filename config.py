import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("url")
login = os.getenv("login")
password = os.getenv("password")