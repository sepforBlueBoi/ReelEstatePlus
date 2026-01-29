#player intizialzation.
from colorama import Fore, init, Style
import time
import os
from REP.core.analysis import analysis

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear' )

init(autoreset=True)

def menu():
    while True:
        print(Fore.YELLOW + "Reel ") #fancy reel estate + intro
        time.sleep(0.4) 
        clear_console()
        print(Fore.YELLOW + "Reel Estate+")
        time.sleep(0.4)
        clear_console()
        print(Fore.YELLOW + "Reel Estate+ !")
    
        # choices {                                                                                       
        time.sleep(0.5)
        print("1. Start Game") # sends to file select
        time.sleep(0.3)
        print("2. Credits") #shows credits(1 person LOL)
        time.sleep(0.3)
        print("3. Not Settings") #NOT settings
        time.sleep(0.3)
        print("4. DLC["+ Fore.RED +"Not available."+ Style.RESET_ALL +"]") #DLC in future?
    
    
        analysis()
    
    
    
def presents():
    clear_console()
    print(Fore.LIGHTCYAN_EX + "SnowMan games " + Style.RESET_ALL + "A Reel Estate remake: " # COLOR
          "\n" + Fore.YELLOW + "Reel Estate+ !")
    print("v-beta")
    for x in range(3):
        print('.', end=' ')
        time.sleep(0.6)# load time.
    print("Press Enter to continue")
    input()
    clear_console()
    menu() # this way it can be used later :). just...cant use calls with args unless you somehow know a way.


if __name__ == "__main__":
    presents()