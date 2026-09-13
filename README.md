# ML-IDS

[![Tests](https://github.com/abdulrhmansaad456eg/ML-IDS/actions/workflows/tests.yml/badge.svg)](https://github.com/abdulrhmansaad456eg/ML-IDS/actions/workflows/tests.yml)

### Real-Time Behavioral Intrusion Detection System Powered by Machine Learning

ML-IDS is a real-time network intrusion detection system that uses a **Random Forest classifier** to detect:

- Port Scanning Attacks
- DDoS Attacks

The system performs live packet sniffing and visualizes threats on a Streamlit dashboard.

---

# How to Run (Step-by-Step)

## Step 1: Train the Model
Training must run once before detection works.

```bash
cd IDS
python train_model.py
```

This generates the trained model file used for attack detection.

---

## Step 2: Start the Packet Sniffer
Run this in a terminal with **Administrator (Windows)** or **sudo (Linux/Mac)** privileges.

```bash
python sniffer.py
```

This begins live packet monitoring and behavioral analysis.

---

## Step 3: Launch the Dashboard
Open a new terminal window and start the Streamlit UI:

```bash
streamlit run dashboard.py
```

A browser tab will open at:

```
http://localhost:8501
```

---

## Step 4: Test the Detection System
Run the simulated attack script to trigger detection.

```bash
python attack.py
```

You should see live threat alerts appear on the dashboard.

---

# How the Model Makes Decisions

The Random Forest model analyzes three core behavioral features:

### Packet Length
Detects unusually small reconnaissance packets often used in port scanning.

### Destination Port
Flags traffic targeting random or high-numbered ports.

### Protocol Type
Learns the difference between:
- TCP (Web traffic / potential attack patterns)
- UDP (System or streaming traffic)

---

# Live Dashboard

The Streamlit dashboard shows real-time monitoring of:

- Total Packets Analyzed
- Threat Percentage
- Top Attacker IP Addresses
- Live Event Logs

---

# Project Architecture

```
train_model.py   → Trains the Random Forest model
sniffer.py       → Captures and analyzes live packets
dashboard.py     → Visualizes live threat telemetry
attack.py        → Simulates malicious behavior
```

---

# Requirements

Install dependencies before running:

```bash
pip install -r IDS/requirements.txt
```

If using Windows, make sure **Npcap** is installed for packet sniffing.
