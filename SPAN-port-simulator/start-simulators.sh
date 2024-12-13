
#!/bin/bash

# Create a new tmux session named 'span-sim' if it doesn't exist
tmux new-session -d -s span-sim

# Split the window into panes for each simulator
tmux split-window -h
tmux split-window -v
tmux select-pane -t 0
tmux split-window -v
tmux select-pane -t 2
tmux split-window -v
tmux select-pane -t 4
tmux split-window -v
tmux select-pane -t 0
tmux split-window -v

# Run a simulator in each pane
tmux select-pane -t 0
tmux send-keys "python Authentication-Log-Anomalies.py" C-m
tmux select-pane -t 1
tmux send-keys "python Firmware-Vulnerability-Check.py" C-m
tmux select-pane -t 2
tmux send-keys "python Packet-Inspection-Anomalies.py" C-m
tmux select-pane -t 3
tmux send-keys "python Real-Time-AI-Driven-Alert-Validation.py" C-m
tmux select-pane -t 4
tmux send-keys "python Session-Hijacking-Attempt.py" C-m
tmux select-pane -t 5
tmux send-keys "python Traffic-Pattern-Anomalies.py" C-m
tmux select-pane -t 6
tmux send-keys "python Unusual-Device-Communication-Patterns.py" C-m

# Attach to the session
tmux attach-session -t span-sim