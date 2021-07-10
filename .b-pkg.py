#!/bin/python3
#This is my first project with python
#special thanks to Tahmid Rayat(htr-tech), google, youtube, kite.com
import os,sys,time,requests
from colorama import init, Fore, Back, Style
init(autoreset=True)
'''
try:
    import requests
except ImportError:
    if sys.version_info[0] == 2:
        os.system('pip2 install requests')
    elif sys.version_info[0] == 3:
        os.system('pip3 install requests')
    else:
        sys.exit("Unable to Install requests. Try 'pip install requests'")

try:
	import colorama
except ImportError:
	if sys.version_info[0] == 2:
		os.system('pip2 install colorama')
	elif sys.version_info[0] == 3:
		os.system('pip3 install colorama')
	else:
		sys.exit("Unable to Install colorama. Try 'pip install colorama'")
from colorama import init, Fore, Back, Style
init(autoreset=True)'''

os.system('clear')
bpkg = '''

██████╗░░░░░░░██████╗░██╗░░██╗░██████╗░ 
██╔══██╗░░░░░░██╔══██╗██║░██╔╝██╔════╝░ 
██████╦╝█████╗██████╔╝█████═╝░██║░░██╗░ 
██╔══██╗╚════╝██╔═══╝░██╔═██╗░██║░░╚██╗ 
██████╦╝░░░░░░██║░░░░░██║░╚██╗╚██████╔╝ 
╚═════╝░░░░░░░╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░ 
'''
print(Fore.BLUE + bpkg)
#Checking Internet Connection...
print("Checking Internet..")
time.sleep(1)
print("")
url = "https://www.google.com"

timeout = 5
try:
	request = requests.get(url, timeout=timeout)
	print(Fore.GREEN + "Connected to the Internet")
except (requests.ConnectionError, requests.Timeout) as exception:
	sys.exit("No internet connection.")
time.sleep(1)
print("")
print(Fore.YELLOW + "Updating Your Termux....")
print("")
os.system("apt update && apt upgrade -y")
time.sleep(1)
print("")
print("")
print(Fore.GREEN + "installing small  basic packages for you:)....")
time.sleep(1)
os.system("apt install git wget figlet ruby cowsay -y")
print(Fore.RED + "Installing Big important packages")
os.system("apt install python python2 php rust apache2 -y")
print("")
print("")
print("")
print(Fore.RED + "Installing important python modules")
os.system("pip2 install --upgrade pip")
os.system("pip3 install --upgrade pip")
os.system("pip2 install  bs4 requests mechanize tqdm colorama")
os.system("pip3 install bs4 requests mechanize tqdm colorama")
time.sleep(1)
print("")
print(Fore.BLUE + "Done installing all packages")
print("")
print("")
print("")
os.system('clear')
banner = '''

██╗░░░░░████████╗ 
██║░░░░░╚══██╔══╝ 
██║░░░░░░░░██║░░░ 
██║░░░░░░░░██║░░░ 
███████╗░░░██║░░░ 
╚══════╝░░░╚═╝░░░ 
'''
print(Fore.RED  + banner)
print("")
print(Fore.CYAN +"CODE writed BY " + Fore.GREEN + "BD" + Fore.RED + "haCkers009")
print("")
print(Fore.YELLOW + "Special Thanks To " + Fore.BLUE + Back.WHITE + "Tahmid Rayat(Htr-tech)")
print("")
