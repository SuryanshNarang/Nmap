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
```python
import nmap

scanner = nmap.PortScanner()
ip_address = input('Enter the IP address you want to scan: ')
resp = input("""\nPlease enter the type of scan you want to run:
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan
                Your choice: """)

if resp == '1':
    scanner.scan(ip_address, '1-1024', '-v -sS')
    print("Open TCP Ports:", scanner[ip_address]['tcp'].keys())
elif resp == '2':
    scanner.scan(ip_address, '1-1024', '-v -sU')
    print("Open UDP Ports:", scanner[ip_address]['udp'].keys())
elif resp == '3':
    scanner.scan(ip_address, '1-1024', '-v -sS -sV -sC -A -O')
    print("Open TCP Ports:", scanner[ip_address]['tcp'].keys())
else:
    print('Please enter a valid option')

