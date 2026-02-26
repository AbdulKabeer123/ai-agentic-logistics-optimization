import random
from services.weather_service import get_weather
from services.traffic_service import get_eta

class Vehicle:
    def __init__(self, vid, start_coords, end_coords):
        self.id = vid
        self.start_coords = start_coords
        self.end_coords = end_coords
        self.eta = 0
        self.weather = None
        self.freshness = 0
        self.urban_event = "normal"

    def update(self):
        # Base ETA
        self.eta = get_eta(self.start_coords, self.end_coords)

        # Real-time weather
        self.weather = get_weather(self.end_coords[0], self.end_coords[1])

        # Urban events simulation (realistic probability)
        event_probabilities = ["normal"] * 5 + ["protest"] + ["construction"]
        self.urban_event = random.choice(event_probabilities)

        # Traffic multiplier
        multiplier = 1.0
        if self.weather:
            if "rain" in self.weather:
                multiplier += 0.3
            elif "storm" in self.weather or "thunderstorm" in self.weather:
                multiplier += 0.5

        if self.urban_event == "protest":
            multiplier += 0.4
        elif self.urban_event == "construction":
            multiplier += 0.2

        # Apply multiplier to ETA
        self.eta *= multiplier
        self.eta = round(self.eta, 2)

        # Freshness (3-hour shelf-life)
        self.freshness = max(0, 1 - (self.eta / 180)) * 100
        self.freshness = round(self.freshness, 2)


class Fleet:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def update_all(self):
        for v in self.vehicles:
            v.update()

    def best_vehicle(self):
        return max(self.vehicles, key=lambda v: v.freshness)