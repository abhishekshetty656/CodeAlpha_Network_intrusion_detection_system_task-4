from scapy.all import sniff
from scapy.layers.inet import IP, TCP

# Suspicious ports
suspicious_ports = [21, 22, 23, 445]

# Function to analyze packets
def detect_intrusion(packet):

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        print("\n==============================")
        print("Packet Detected")
        print("==============================")
        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")

        # Check TCP packets
        if packet.haslayer(TCP):

            port = packet[TCP].dport

            print(f"Destination Port : {port}")

            # Detect suspicious ports
            if port in suspicious_ports:

                alert_message = (
                    f"ALERT! Suspicious activity detected!\n"
                    f"Source IP: {src_ip}\n"
                    f"Destination IP: {dst_ip}\n"
                    f"Port: {port}\n"
                )

                print("\n⚠ ALERT: Suspicious Port Activity Detected!")

                # Save alerts to file
                with open("alerts.txt", "a") as file:
                    file.write(alert_message + "\n")

# Start IDS
print("Starting Intrusion Detection System...")
print("Monitoring Network Traffic...\n")

sniff(prn=detect_intrusion, count=20)

print("\nMonitoring Completed!")