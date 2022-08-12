import socket
import threading
import sys
print("-"*50)
Banner = "Welcome To CyBenSec Port Scanning"
Sub = "Enter Ip address to scan"
print(Banner.center(20))
print(Sub.center(22))
print("-"*50)
target = input("Enter Target ip address : ").strip()

try:
    target_ip = socket.gethostbyname(target)
except:
    socket.gaierror
    sys.exit()
def scan_port(port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    connection = s.connect_ex((target_ip,port))
    if connection == 0:
        print(f"Port {port} is Open")
        s.close()
for port in range(65536):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
print("Scanning has Ended Thank you vist again :-)")

