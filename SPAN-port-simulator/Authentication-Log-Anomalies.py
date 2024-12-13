import json
import time

def simulate_auth_logs():
    with open("authentication-log-anomalies.json", "r") as f:
        data = json.load(f)
    for entry in data:
        print(entry)
        time.sleep(0.5)

if __name__ == "__main__":
    simulate_auth_logs()
