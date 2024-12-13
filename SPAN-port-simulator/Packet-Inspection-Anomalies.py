import json
import time

def simulate_packet_inspection():
    with open("packet_inspection_anomalies.json", "r") as f:
        data = json.load(f)
    for entry in data:
        print(entry)
        time.sleep(0.5)

if __name__ == "__main__":
    simulate_packet_inspection()
