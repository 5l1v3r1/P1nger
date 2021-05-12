#Feel free to look at all of the code which is only 43 lines and is pretty basic

import colorama
import os
import time

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

def ipping():
    os.system("cls")
    count = 1
    e = input("P1nger Target:   ")
    replies = 0
    replies += 1
    hostname = e
    os.system("cls")
    print("-"*100)
    print("="*100)
    print("-"*100)
    while True:
        response = os.system("ping -n 1 " + hostname + " >nul")
        if response == 0:
            print("\033[1;32;40m" + hostname + " is being P1NGED" + " [" +  str(count) + "]" +  '\033[0m')
        else:
            print("\033[31m" + hostname + " offline" " [" +  str(count) + "]" +  '\033[0m')
        count += 1
        time.sleep(1)


ipping()
