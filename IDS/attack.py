from scapy.all import IP, TCP, send
import time
import random

print("⚔️ Starting simulated Port Scan attack...")
target = "127.0.0.1"

# Hit 50 random ports with tiny packets
for i in range(50):
    port = random.randint(20000, 60000)
    pkt = IP(dst=target)/TCP(dport=port)/"SCAN"
    send(pkt, verbose=False)
    print(f"Scanning port {port}...")
    time.sleep(0.1)

print("✅ Attack simulation complete.")