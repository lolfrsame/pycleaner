

from random import randint
from pystyle import Colors, Colorate, Center
import base64
import os
import time
import requests
import subprocess
from colorama import Fore
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from pathlib import Path
import platform
import sys

tools = os.getcwd()+"\\tools\\"
if not os.path.exists(tools):
    os.mkdir(tools)
# THIS CREATES THE TOOLS DIRECTORY IN THE SAME DIRECTORY, IF IT DOES NOT EXIST, IN WHICH THE PYTHON SCRIPT IS RAN. 
ver = Center.XCenter('''

██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗  ░░███╗░░░░░░░███╗░░
██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║  ░████║░░░░░░████║░░
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║  ██╔██║░░░░░██╔██║░░
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║  ╚═╝██║░░░░░╚═╝██║░░
░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║  ███████╗██╗███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝  ╚══════╝╚═╝╚══════╝''')
__author__ = 'dynasty' 
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
os.system("title fr cleaner")

banner = Center.XCenter("""
ver 1.1
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
11.)   more info
12.)   exit
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
    #more info
    elif choice == '11':
        os.system('cls')
        print(Colors.red, "                                   made by dynasty and curd ", )
        version = sys.getwindowsversion()
        print(platform.platform())
        print(version)
        print(platform.system())
        print(platform.release())
        print(platform.version())
        print(platform.version().split('.')[2]) 
        print((platform.machine())+ ' bit' )
        username = os.getlogin()
        print('ur username is ' +   username)
        print (ver)
        input("Press Enter to continue...")
        main()
    #exit
    elif choice == '12':
       os._exit(0) 
    #else       
    else:
        print("That ain't an option\n")
        print("RESTARTING!!!")
        time.sleep(2)
        main()
    main()

if __author__ != 'dynasty':
    print("AN ERROR HAS OCCURED")
    os._exit(0)

main()
