import random
from services.traffic_service import get_eta
from services.weather_service import get_weather

# --- Freshness Score Function ---
def freshness_score(eta, shelf_life=180):
    score = max(0, 1 - (eta / shelf_life)) * 100
    return round(score, 2)

# --- Karachi Coordinates ---
warehouse = (24.8607, 67.0011)  # Saddar, Karachi
dha = (24.8138, 67.0330)        # DHA, Karachi

# --- Calculate Base ETA (Real-Time Routing) ---
eta = get_eta(warehouse, dha)

# --- Get Real-Time Weather for Destination ---
weather = get_weather(dha[0], dha[1])

# --- Simulate Karachi Urban Disruptions (Realistic Probability) ---
event_probabilities = ["normal"] * 5 + ["protest"] + ["construction"]
event = random.choice(event_probabilities)

traffic_multiplier = 1.0

# --- Weather-Based Delay ---
if weather:
    if "rain" in weather:
        traffic_multiplier += 0.3  # +30% delay
    elif "storm" in weather or "thunderstorm" in weather:
        traffic_multiplier += 0.5  # +50% delay

# --- Urban Event-Based Delay ---
if event == "protest":
    traffic_multiplier += 0.4  # +40% delay
elif event == "construction":
    traffic_multiplier += 0.2  # +20% delay

# --- Apply Total Traffic Multiplier ---
eta *= traffic_multiplier
eta = round(eta, 2)

# --- Calculate Freshness Score (3-Hour Shelf Life) ---
score = freshness_score(eta)

# --- Output Results ---
print(f"Weather Condition: {weather}")
print(f"Urban Event: {event}")
print(f"Adjusted ETA (minutes): {eta}")
print(f"Freshness Score: {score}%")