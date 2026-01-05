import pandas as pd
import os

def load_data():
    matches_path = os.path.join("data", "matches.csv")
    deliveries_path = os.path.join("data", "deliveries.csv")

    if not os.path.exists(matches_path):
        raise FileNotFoundError("matches.csv not found in data folder")

    if not os.path.exists(deliveries_path):
        raise FileNotFoundError("deliveries.csv not found in data folder")

    matches = pd.read_csv(matches_path)
    deliveries = pd.read_csv(deliveries_path)

    return matches, deliveries
