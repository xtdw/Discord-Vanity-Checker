import requests
import os
from colorama import Fore
import time

def checkTxt(vanity):
    with open("./available.txt", 'r') as f:
        available = f.readlines()
    return any(f"discord.gg/{vanity}\n" == line for line in available)

def check(vanity):
    if checkTxt(vanity):
        print(f"{Fore.BLUE} Vanity {vanity} already exists in 'available.txt'{Fore.RESET}")
        return
    url = f'https://discord.com/api/v8/invites/{vanity}?with_counts=true'
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f'{Fore.RED}Vanity {vanity} is unavailable{Fore.RESET}')
    elif response.status_code == 404:
        print(f'{Fore.GREEN}Vanity {vanity} is available{Fore.RESET}')
        with open('available.txt', 'a') as file:
            file.write(f"discord.gg/{vanity}\n")
    else:
        print(f'{Fore.YELLOW}Failed to check vanity {vanity}. Status code: {response.status_code}{Fore.RESET}')

def checkM():
    vanity = input(f'{Fore.CYAN}Enter a vanity: {Fore.RESET}')
    print("\nChecking...\n")
    check(vanity)

def checkF():
    with open('vanities.txt', 'r') as file:
        vanities = file.readlines()
    
    print("\nChecking vanities from vanities.txt\n")
    
    for vanity in vanities:
        vanity = vanity.strip()
        check(vanity)
        time.sleep(0.5)
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{Fore.RED}[1] Manually enter vanity')
    print(f'[2] Check vanities from file (vanities.txt){Fore.RESET}')
    choice = input(f'{Fore.YELLOW}Enter your choice: {Fore.RESET}')
    
    if choice == '1':
        checkM()
    elif choice == '2':
        checkF()
    else:
        print(f'{Fore.RED}[ERROR] Invalid choice.{Fore.RESET}')

if __name__ == '__main__':
    main()
