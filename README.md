# Network Intrusion Detection System (NIDS)

## Project Overview

This project demonstrates a basic Network Intrusion Detection System (NIDS) developed using Python and the Scapy library. The system monitors live network traffic, analyzes packets, detects suspicious port activities, and generates intrusion alerts.

The project helps in understanding network monitoring, packet analysis, intrusion detection techniques, and cybersecurity concepts.

---

# Objectives

* Monitor live network traffic
* Detect suspicious network activities
* Generate intrusion alerts
* Analyze network packets
* Understand intrusion detection concepts
* Implement basic cybersecurity monitoring techniques

---

# Technologies Used

* Python
* Scapy
* VS Code
* Npcap
* GitHub

---

# Project Structure

```text id="rd1"
Network_Intrusion_Detection_System/
│
├── ids.py
├── alerts.txt
├── screenshots/
├── report.pdf
└── README.md
```

---

# Features

* Real-time packet monitoring
* Suspicious port detection
* Intrusion alert generation
* Alert logging system
* Packet analysis
* Beginner-friendly IDS implementation

---

# Suspicious Ports Monitored

| Port Number | Service |
| ----------- | ------- |
| 21          | FTP     |
| 22          | SSH     |
| 23          | Telnet  |
| 445         | SMB     |

These ports are commonly targeted by attackers for unauthorized access and network exploitation.

---

# How the IDS Works

The Intrusion Detection System performs the following operations:

1. Captures live network packets
2. Analyzes source and destination IP addresses
3. Checks TCP destination ports
4. Detects suspicious network activities
5. Generates alerts
6. Stores intrusion logs inside `alerts.txt`

Whenever suspicious traffic is detected, the system displays warning messages and logs intrusion details.

---

# Installation

## Step 1 — Install Python

Download Python from:
https://www.python.org/downloads/

---

## Step 2 — Install Scapy

Open terminal and run:

```bash id="rd2"
pip install scapy
```

---

## Step 3 — Install Npcap (Windows)

Download from:
https://npcap.com/#download

During installation enable:

* Install Npcap in WinPcap API-compatible Mode

Restart the system after installation.

---

# How to Run the Project

Open terminal inside the project folder and run:

```bash id="rd3"
python ids.py
```

Generate network traffic by:

* Opening websites
* Running ping commands

Example:

```bash id="rd4"
ping google.com
```

---

# Sample Output

```text id="rd5"
Packet Detected

Source IP      : 192.168.1.5
Destination IP : 142.250.183.78
Destination Port : 445

⚠ ALERT: Suspicious Port Activity Detected!
```

---

# Learning Outcome

Through this project, I learned about:

* Packet analysis
* Network monitoring
* Intrusion detection systems
* Suspicious port analysis
* Alert generation
* Cybersecurity implementation using Python

---

# Advantages

* Simple IDS implementation
* Real-time monitoring
* Intrusion detection alerts
* Practical cybersecurity project
* Beginner-friendly implementation

---

# Limitations

* Basic intrusion detection only
* No machine learning detection
* No advanced malware analysis
* No graphical dashboard

---

# Future Improvements

Future enhancements may include:

* Machine learning-based detection
* Email notifications
* Automatic IP blocking
* Dashboard visualization
* Database integration

---

# Conclusion

This project successfully implemented a basic Python-based Network Intrusion Detection System using Scapy. The IDS monitored live network traffic, detected suspicious activities, generated alerts, and improved understanding of cybersecurity monitoring techniques.

---

# References

* Python Official Documentation
* Scapy Documentation
* OWASP Network Security Guidelines

---

# Author

Abhishek
