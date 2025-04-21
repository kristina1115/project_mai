import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("url")
login = os.getenv("login")
password = os.getenv("password")

audience_name = os.getenv("audience_name")
audience_changed_name = os.getenv("audience_changed_name")
other_audience_name = os.getenv("other_audience_name")
indicator_1 = os.getenv("indicator_1")
indicator_2 = os.getenv("indicator_2")
indicator_3 = os.getenv("indicator_3")
indicator_4 = os.getenv("indicator_4")
