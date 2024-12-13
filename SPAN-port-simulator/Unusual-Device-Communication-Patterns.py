import json
import time

def simulate_unusual_comm():
    with open("unusual_device_comm_patterns.json", "r") as f:
        data = json.load(f)
    for entry in data:
        print(entry)
        time.sleep(0.5)

if __name__ == "__main__":
    simulate_unusual_comm()
