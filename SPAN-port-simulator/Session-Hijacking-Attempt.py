import json
import time

def simulate_session_hijack():
    with open("session_hijack_attempts.json", "r") as f:
        data = json.load(f)
    for entry in data:
        print(entry)
        time.sleep(0.5)

if __name__ == "__main__":
    simulate_session_hijack()
