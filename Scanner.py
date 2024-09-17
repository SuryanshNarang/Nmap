import nmap
scanner = nmap.PortScanner()
print('Welcome, this is a simple nmap automation tool developed by Suryansh Narang')
print('<------------------------------------------------------------------------>')

ip_address= input('Enter the IP address you want to scan: ')
print('The IP address you entered is', ip_address)
type(ip_address)

resp = input("""\nPlease enter the type of scan you want to run:
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan
                Your choice: """)
print('You have selected the option: ', resp)

if resp=='1':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_address,'1-1024','-v -sS')  #starting the scan.
    print(scanner.scaninfo()) #printing scan info to the user
    print("IP Status: ",scanner[ip_address].state()) #wether an ipaddress is 'up' or not.
    print(scanner[ip_address].all_protocols()) #protocols tcp or udp
    print("The open ports are going to be: ", scanner[ip_address]['tcp'].keys())    
elif resp == '2':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sU')  # UDP scan
    print(scanner.scaninfo())  # Printing scan info to the user
    print("IP Status: ", scanner[ip_address].state())  # Whether an IP address is 'up' or not
    print(scanner[ip_address].all_protocols())  # Protocols (tcp or udp)
    print("The open ports are going to be: ", scanner[ip_address]['udp'].keys()) 
elif resp == '3':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS -sV -sC -A -O')  # Comprehensive scan
    print(scanner.scaninfo())  # Printing scan info to the user
    print("IP Status: ", scanner[ip_address].state())  # Whether an IP address is 'up' or not
    print(scanner[ip_address].all_protocols())  # Protocols (tcp or udp)
    print("The open ports are going to be: ", scanner[ip_address]['tcp'].keys())
elif resp=>'4':
    print('Please enter a valid option')