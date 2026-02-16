#  ML-IDS  
### Real-Time Behavioral Intrusion Detection System Powered by Machine Learning

ML-IDS is a real-time network intrusion detection system that uses a **Random Forest classifier** to detect:

-  Port Scanning Attacks  
-  DDoS Attacks  

The system performs live packet sniffing and visualizes threats through a high-tech Streamlit dashboard.

---

#  How to Run (Step-by-Step)

##  Step 1: Train the AI Model
You must create the "Brain" before detection can begin.

```bash
python train_model.py
```

This generates the trained Machine Learning model used for attack detection.

---

##  Step 2: Start the Packet Sniffer Engine
Run this in a terminal with **Administrator (Windows)** or **sudo (Linux/Mac)** privileges.

```bash
python engine.py
```

This begins live packet monitoring and behavioral analysis.

---

##  Step 3: Launch the Dashboard
Open a new terminal window and start the Streamlit UI:

```bash
streamlit run dashboard.py
```

A browser tab will automatically open at:

```
http://localhost:8501
```

---

##  Step 4: Test the Detection System
Run the simulated attack script to trigger malicious behavior detection.

```bash
python attack.py
```

You should see live threat alerts appear on the dashboard.

---

#  How the AI Makes Decisions

The Random Forest model analyzes three core behavioral features:

###  Packet Length
Detects unusually small reconnaissance packets often used in port scanning.

###  Destination Port
Flags traffic targeting random or high-numbered ports.

### Protocol Type
Learns the difference between:
- TCP (Web traffic / potential attack patterns)
- UDP (System or streaming traffic)

---

#  Live Telemetry Dashboard

The Streamlit dashboard provides real-time monitoring of:

-  Total Packets Analyzed  
-  Threat Percentage  
-  Top Attacker IP Addresses  
-  Live Event Logs  

---

#  Project Architecture

```
train_model.py      → Trains the Random Forest model  
engine.py     → Captures and analyzes live packets  
dashboard.py  → Visualizes live threat telemetry  
attack.py     → Simulates malicious behavior  
```

---

#  Requirements

Install dependencies before running:

```bash
pip install pandas numpy scikit-learn scapy streamlit matplotlib plotly
```

If using Windows, make sure **Npcap** is installed for packet sniffing.

---

# Author

Real-Time Behavioral ML Intrusion Detection System  
Built with Python, Scapy, Scikit-Learn, and Streamlit
