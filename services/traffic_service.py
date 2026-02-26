import requests
import os
from dotenv import load_dotenv

load_dotenv()

ORS_API_KEY = os.getenv("ORS_API_KEY")

BASE_URL = "https://api.openrouteservice.org/v2/directions/driving-car"


def get_eta(start_coords, end_coords):
    headers = {
        "Authorization": ORS_API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "coordinates": [
            [start_coords[1], start_coords[0]],  # ORS expects [lng, lat]
            [end_coords[1], end_coords[0]]
        ]
    }

    response = requests.post(BASE_URL, json=body, headers=headers)

    if response.status_code != 200:
        print("Error:", response.text)
        return None

    data = response.json()
    duration_seconds = data["routes"][0]["summary"]["duration"]

    duration_minutes = duration_seconds / 60

    return round(duration_minutes, 2)