import json
import time

def simulate_ai_alert_validation():
    with open("ai_alert_validation.json", "r") as f:
        data = json.load(f)
    for entry in data:
        print(entry)
        time.sleep(0.5)

if __name__ == "__main__":
    simulate_ai_alert_validation()
