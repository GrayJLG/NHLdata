import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NHL_API_KEY")

# gameid I want to use
game_id = 22335

BASE_URL = f"https://replay.sportsdata.io/api/v3/nhl/pbp/json/playbyplay/{game_id}?key={API_KEY}"

response = requests.get(BASE_URL)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")
