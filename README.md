# Nmap Automation Tool

Welcome to my Nmap automation tool! This tool simplifies network scanning using Nmap, providing quick insights into open ports and services running on a target system.

## Features:
- **SYN ACK Scan:** Fast and stealthy scan using TCP SYN packets.
- **UDP Scan:** Detection of open UDP ports and associated services.
- **Comprehensive Scan:** Detailed scan including version detection, script scanning, OS detection, and more.

## How to Use:
1. **Enter IP Address:** Input the IP address you want to scan.
2. **Select Scan Type:** Choose from SYN ACK Scan, UDP Scan, or Comprehensive Scan.
3. **View Results:** Detailed results include open ports, detected protocols, and IP status.

## Example Usage:
```bash
Welcome, this is a simple nmap automation tool developed by Suryansh Narang
<------------------------------------------------------------------------>

Enter the IP address you want to scan: 192.168.1.1
The IP address you entered is 192.168.1.1

Please enter the type of scan you want to run:
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan
                Your choice: 1
You have selected the option:  1
Nmap version:  (7, 91)
{'tcp': {'method': 'syn', 'services': '1-1024'}}
IP Status:  up
['tcp']
The open ports are going to be:  dict_keys([22, 80, 443])
