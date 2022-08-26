#!  usr/bin/python3.10.6

import socket
import threading
import sys
import time

#Welcome banner
print("-"*50)
Banner = "Welcome To CyBenSec Port Scanning"
Sub = "Enter Ip address or Domain to scan"
print(Banner.center(20))
print(Sub.center(22))
print("-"*50)

#storing user input as userinput

userinput=input("Target : ").strip()
port_list=[]
#name resolution error handling
try:
    target_ip = socket.gethostbyname(userinput)
    print(f"The IP address acquired from {userinput} is {target_ip}")
except:
    socket.gaierror
    sys.exit()

#defining scan function
def scan_port(port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    connection = s.connect_ex((target_ip,port))
    if connection == 0:
        port_list.append(port)
        s.close()
print(f"Scanning for {userinput} is in progress......")
#implementing scan funcation with all ports(65536) at a time using threading
for port in range(65536):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()

time.sleep(0.3)
print("Thank you For your patience")
time.sleep(0.3)
for result in port_list:
    print(f"Port{result} is Open")
    time.sleep(0.3)
print("Scanning has Ended Thank you vist again :-)")

