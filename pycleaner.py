import threading
from tkinter import font
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from random import randint
import base64
import os
import time
import subprocess
from colorama import Fore
from pathlib import Path
import platform
import sys
import shutil
import pathlib
try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    import pystyle
except:
    os.system("pip install pystyle")
    import pystyle

try:
    import colorama
except:
    os.system("pip install colorama")
    import colorama

try:
    from colorama import Fore
except:
    os.system("pip install Fore")
    from colorama import Fore

try:
    from pystyle import Colors, Colorate, Center
except:
    os.system("pip install pystyle")
    from pystyle import Colors, Colorate, Center
try:
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
except:
    os.system("pip install pystyle")
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System



username = os.getlogin()

tools = os.getcwd()+"\\tools\\"
if not os.path.exists(tools):
    os.mkdir(tools)
# THIS CREATES THE TOOLS DIRECTORY IN THE SAME DIRECTORY, IF IT DOES NOT EXIST, IN WHICH THE PYTHON SCRIPT IS RAN. 
ver = Center.XCenter('''
██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗  ░░███╗░░░░░██████╗░
██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║  ░████║░░░░░╚════██╗
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║  ██╔██║░░░░░░░███╔═╝
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║  ╚═╝██║░░░░░██╔══╝░░
░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║  ███████╗██╗███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝  ╚══════╝╚═╝╚══════╝''')
__author__ = 'Dynasty' 
os.system("title PRESS ENTER")

banner = r'''
███████╗██████╗░  ░█████╗░██╗░░░░░███████╗░█████╗░███╗░░██╗███████╗██████╗░
██╔════╝██╔══██╗  ██╔══██╗██║░░░░░██╔════╝██╔══██╗████╗░██║██╔════╝██╔══██╗
█████╗░░██████╔╝  ██║░░╚═╝██║░░░░░█████╗░░███████║██╔██╗██║█████╗░░██████╔╝
██╔══╝░░██╔══██╗  ██║░░██╗██║░░░░░██╔══╝░░██╔══██║██║╚████║██╔══╝░░██╔══██╗
██║░░░░░██║░░██║  ╚█████╔╝███████╗███████╗██║░░██║██║░╚███║███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝  ░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
by dynasty
'''

System.Size(120, 30)
System.Clear()
Anime.Fade(Center.XCenter(banner), Colors.rainbow, Colorate.Vertical, interval=0.025, enter=True)
os.system("title  Hello, "+   username)

banner = Center.XCenter("""
ver 1.2
███████╗██████╗░  ░█████╗░██╗░░░░░███████╗░█████╗░███╗░░██╗███████╗██████╗░
██╔════╝██╔══██╗  ██╔══██╗██║░░░░░██╔════╝██╔══██╗████╗░██║██╔════╝██╔══██╗
█████╗░░██████╔╝  ██║░░╚═╝██║░░░░░█████╗░░███████║██╔██╗██║█████╗░░██████╔╝
██╔══╝░░██╔══██╗  ██║░░██╗██║░░░░░██╔══╝░░██╔══██║██║╚████║██╔══╝░░██╔══██╗
██║░░░░░██║░░██║  ╚█████╔╝███████╗███████╗██║░░██║██║░╚███║███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝  ░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
by dynasty\n
""")


options = """
         OPTIONS\n
1.)    temp cleaner
2.)    log cleaner
3.)    disable services 
4.)    Services Optimization
5.)    battery check (laptops only)
6.)    turn on hibernate
7.)    tree (better Responsiveness)
8.)    Delete Windows Update Cache
9.)    disable windows defender
10.)   update 
11.)   removes tools folder with files
12.)   more info
13.)   exit
"""
def download(url, name):
    response =  requests.get(url)
    open(tools+name, "w").write(response.text)
    os.startfile(tools+name)
    
    # THIS DOWNLOADS THE BAT FILES TO THE TOOLS DIRECTORY. THIS TAKES THE URL AND THE NAME OF THE BAT FILE.

def main():
    os.system('cls')
    print(Colorate.Vertical(Colors.blue_to_red, banner + options, 2))
    choice = input(Colors.green + 'Which option do you choose? ->  ')
    #temp
    if choice == '1':
        download  ("https://untimelyimpressionableadministration.blus2tlia.repl.co/temp.bat", "temp_cleaner.bat")
        time.sleep(5)
        os.rmdir('temp')
        os.rmdir('prefetch')
        
    #log cleaner
    elif choice == '2':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/log%20cleaner.bat", "log_cleaner.bat")
       
    #disable services
    elif choice == "3":
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/services.bat", "disable_services.bat")
  
    #service_optimizer
    elif choice == "4":
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/optimization.bat", "service_optimizer.bat")

    #battery_check
    elif choice == '5':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/battery.bat", "battery_check.bat")
 
    #hibernate
    elif choice == '6':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/hibernate.bat", "hibernate.bat")

    #tree
    elif choice == '7':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/tree.bat", "tree.bat")

    #windows update
    elif choice == '8':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/update.cmd", "delete_windows_update_cache.cmd")

    #disable_services
    elif choice == '9':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/def.reg", "disable_windows_defender.reg")
 
    #update
    elif choice == '10':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/updater.bat", "update.bat")
    #tools
    elif choice == '11':
       shutil.rmtree("tools")         
       main()
       
    #more info
    elif choice == '12':
        os.system('cls')
        print(Colors.purple, "                                   made by dynasty and curd ", )
        version = sys.getwindowsversion()
        print(platform.platform())
        print(version)
        print(platform.system())
        print(platform.release())
        print(platform.version())
        print(platform.version().split('.')[2]) 
        print((platform.machine())+ ' bit' )
        print('ur username is ' +   username)
        print (ver)
        input("Press Enter to continue...")
        main()
    #exit
    elif choice == '13': 
        os._exit(0) 
         
    #else       
    else:
        print("That ain't an option\n")
        os.rmdir('temp')  
        os.rmdir('prefetch')  
        print("RESTARTING!!!")
        time.sleep(2)
        main()
    main()

if __author__ != 'Dynasty':
    print("AN ERROR HAS OCCURED")
    os._exit(10)
         
main()
