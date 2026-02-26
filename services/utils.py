# services/utils.py

def freshness_score(eta, shelf_life=180):
    """Calculate freshness score based on ETA and shelf-life in minutes"""
    score = max(0, 1 - (eta / shelf_life)) * 100
    return round(score, 2)