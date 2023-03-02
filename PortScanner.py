import socket
import sys
from datetime import datetime

server = input("Enter a host to scan: ")

#Asking for input
serverIP = socket.gethostbyname(server)

print("_" * 60)
print("Please wait, scanning host ", serverIP)
print("_" * 60)

#Check the date and time the scan was started
t1 = datetime.now()

#Asking for port number range
port1 = input("Enter starting port number:")
port2 = input("Enter ending port number:")

convertedPort1 = int(port1)
convertedPort2 = int(port2)

print("Scanning ports:" , convertedPort1 , "-", convertedPort2)
try:
    for port in range (convertedPort1, convertedPort2):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((serverIP, port))
        print("Port {}: CLOSED".format(port))
        if result == 0:
            print("Port {}: OPEN".format(port))
        sock.close()

except KeyboardInterrupt:
    print("Exiting...")
    sys.exit()

except socket.gaierror:
    print("Hostname count not be resolved. Exiting...")

except socket.error:
    print("Couldn't connect to server. Exiting...")

#Checking the end time
t2 = datetime.now()

total = t2 - t1

print("Scanning completed in:", total)
