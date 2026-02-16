import pandas as pd
import joblib
from scapy.all import sniff, IP, TCP, UDP
import datetime
import os

LOG_FILE = "logs.csv"


model = joblib.load('ids_model.pkl')
scaler = joblib.load('scaler.pkl')

if not os.path.exists(LOG_FILE):
    pd.DataFrame(columns=["timestamp", "src_ip", "dst_port", "packet_len", "prediction"]).to_csv(LOG_FILE, index=False)

print("🕵️ IDS Engine Running... (Admin Mode)")

def analyze_packet(packet):
    if IP in packet:
        try:
            src_ip = packet[IP].src
            pkt_len = len(packet)
            dst_port = packet[TCP].dport if TCP in packet else (packet[UDP].dport if UDP in packet else 0)
            proto = 6 if TCP in packet else (17 if UDP in packet else 0)

            
            feat = pd.DataFrame([[pkt_len, dst_port, proto]], columns=['packet_len', 'dst_port', 'protocol'])
            feat_scaled = scaler.transform(feat)
            pred = model.predict(feat_scaled)[0]
            label = "MALICIOUS" if pred == 1 else "BENIGN"
            
            ts = datetime.datetime.now().strftime("%H:%M:%S")

            
            color = "\033[91m" if label == "MALICIOUS" else "\033[92m"
            print(f"{color}[{label}] {src_ip} -> {dst_port}\033[0m")

            with open(LOG_FILE, "a") as f:
                f.write(f"{ts},{src_ip},{dst_port},{pkt_len},{label}\n")
        except:
            pass

sniff(iface=None, prn=analyze_packet, store=0)