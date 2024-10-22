import platform
import os
import time
from PyFiglet import Figlet
def menu():
    print("[1]")
    print("[2]")
    print("[0] Exit the Program")
    
menu()
option = int(input("Enter your option: "))
def clearWindows():
    os.system('cls')
def clearLinux():
    os.system('clear')

while option != 0: 
    if option == 1:
        #do option 1 stuff
        print("option 1 has been called, clearing after 5 seconds")
        time.sleep(5)
        if platform.system() == "Windows":
            clearWindows()
        else:
            clearLinux()
    elif option == 2:
        #do option 2 stuff
        print("option 2 has been called, clearing after 5 seconds")
        time.sleep(5)
        if platform.system() == "Windows":
            clearWindows()
        else:
            clearLinux()
    else:
        print("Invalid option")
    
    print()
    menu()
    option = int(input("Enter your option: "))

print("Thanks for using Network Fixer, Christ is King!")