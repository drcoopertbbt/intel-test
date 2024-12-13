# SPAN Port Simulator

This repository contains various network traffic and security simulation scripts.

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

## Running the Simulators

Each simulator can be run independently using Python. Make sure your virtual environment is activated before running any script.

```bash
# Authentication Log Anomalies Simulator
# verified working ✅
python Authentication-Log-Anomalies.py

# Firmware Vulnerability Check Simulator
# verified working ✅
python Firmware-Vulnerability-Check.py

# Packet Inspection Anomalies Simulator
# verified working ✅
python Packet-Inspection-Anomalies.py

# Real-Time AI-Driven Alert Validation
# verified working ✅
python Real-Time-AI-Driven-Alert-Validation.py

# Session Hijacking Attempt Simulator
# verified working ✅
python Session-Hijacking-Attempt.py

# Traffic Pattern Anomalies Simulator
python Traffic-Pattern-Anomalies.py

# Unusual Device Communication Patterns Simulator
python Unusual-Device-Communication-Patterns.py
```

Each simulator has an associated JSON configuration file that contains the simulation parameters:
- `authentication-log-anomalies.json`
- `firmware_vulnerability_check.json`
- `packet_inspection_anomalies.json`
- `ai_alert_validation.json`
- `session_hijack_attempts.json`
- `unusual_device_comm_patterns.json`


# Tmux

To run all the simulators in a single window, you can use the `start-simulators.sh` script. This script uses tmux to create a new session with multiple panes, each running a different simulator.

```bash
./start-simulators.sh
```

This script will open a tmux session with 7 panes, each running a different simulator. You can use the tmux commands to navigate between the panes and interact with the simulators.

To exit the tmux session, simply press `Ctrl+D` in the terminal where the tmux session is running.
