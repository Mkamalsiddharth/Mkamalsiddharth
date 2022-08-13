#!usr/bin/python3.10.6

import socket
import threading
import sys

#Welcome banner

print("-"*50)
Banner = "Welcome To CyBenSec Port Scanning"
Sub = "Enter Ip address or Domain to scan"
print(Banner.center(20))
print(Sub.center(22))
print("-"*50)

#storing user input as userinput

userinput=input("Target : ").strip()

#name resolution error handling
try:
    target_ip = socket.gethostbyname(userinput)
except:
    socket.gaierror
    sys.exit()

#defining scan function 
def scan_port(port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    connection = s.connect_ex((target_ip,port))
    if connection == 0:
        print(f"Port {port} is Open")
        s.close()

#implementing scan funcation with all ports(65536) at a time using threading
for port in range(65536):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
print("Scanning has Ended Thank you vist again :-)")

