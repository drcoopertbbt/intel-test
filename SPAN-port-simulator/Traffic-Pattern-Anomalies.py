import json
import time

def simulate_traffic_anomalies():
    with open("traffic_pattern_anomalies.json", "r") as f:
        data = json.load(f)
    while True:
        for entry in data:
            print(entry)
            time.sleep(0.5)

if __name__ == "__main__":
    simulate_traffic_anomalies()
