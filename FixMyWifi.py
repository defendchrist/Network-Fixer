import platform
import subprocess
import os
import time
def menu():
    os.chdir(os.path.dirname(__file__))
    try:
        # Define the list of ASCII art files
        ascii_files = ["NetworkFixerAscii.txt", "NetworkFixerAscii2.txt", "NetworkFixerAscii3.txt", "NetworkFixerAscii4.txt"]

        # Set the console color to green on black
        os.system('color 02')

        # Animate the ASCII art
        for file in ascii_files:
            # Clear the console
            os.system('cls')
            # Open the current ASCII art file
            with open(file, encoding="utf-8") as f:
                # Print the current frame
                print("\033[92m" + f.read() + "\033[0m")
            # Print the menu options
            print("\033[93m" + "By ☠ Defender Of Christ ☦" + "\033[0m")
            
            print("Select an option:")
            print("[1]")
            print("[2]")
            print("[0] Exit the Program")
            # Wait for a short time
            time.sleep(0.4)

        # Reset the console color to default
        os.system('color')

    except FileNotFoundError:
        print("Error: One or more ASCII art files not found.")
        print(os.listdir())

    
menu()
option = int(input("Enter your option: "))
def clearWindows():
    os.system('cls')
def clearLinux():
    os.system('clear')



while option != 0: 
    if option == 1:
        #do option 1 stuff
        print("Restart Network Adapters, clearing after complete")
        import subprocess
        # Get wifi interface name
        output = subprocess.run(["netsh", "wlan", "show", "interfaces"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = output.stdout.decode()
        interface_name = None
        for line in output.splitlines():
            if "Description" in line:
                interface_name = line.split(":")[1].strip()
                break
        # Restart network adapters
        if interface_name:
            # Disable the Wi-Fi interface
            subprocess.run(["netsh", "interface", "set", "interface", "name=" + interface_name, "adminstate=DISABLED"], shell=True)
            # Enable the Wi-Fi interface
            subprocess.run(["netsh", "interface", "set", "interface", "name=" + interface_name, "adminstate=ENABLED"], shell=True)
        else:
            print("Could not find the current Wi-Fi interface name")
        time.sleep(1)
        if platform.system() == "Windows":
            clearWindows()
        else:
            subprocess.run(["sudo", "ifdown", "-a"], shell=True)
            subprocess.run(["sudo", "ifup", "-a"], shell=True)
            clearLinux()



    elif option == 2:
        #do option 2 stuff
        print("Flushing DNS Cache, clearing after complete")
        subprocess.run(["ipconfig", "/flushdns"], shell=True)
        time.sleep(1)
        if platform.system() == "Windows":
            clearWindows()
        else:
            subprocess.run(["sudo", "service", "network-manager", "restart"], shell=True)
            clearLinux()



    else:
        print("Invalid option")



    print()
    menu()
    option = int(input("Enter your option: "))

print("Thanks for using Network Fixer, Christ is King!")