import time
import sys
from colorama import Fore, Style, init

def clear():
    sys.stdout.write("\033[H\033[2J\033[3J")

from REP.Modules.Save_Modules.Load_module import load_json

credit: dict = load_json("lore.json") # loads credits. only time this is called outside the main loop.

def credits():
    print(credit["credit1"]) # Reel Estate+
    time.sleep(0.9)

    credits2 = credit["credit2"].replace("Kondike_Barr", f"{Fore.BLUE}Kondike_Barr{Style.RESET_ALL}") # a blue kondike ;)

    print(credits2) # Made my Kondike
    time.sleep(0.9)
    print(credit["credit3"]) # Special thanks to No2No, Minecraft Man, and FryinnPan
    time.sleep(0.9)
    print(credit["credit4"]) # My last planned Text Based Game
    time.sleep(0.9)
    print(credit["credit5"]) # be looking forewards to Kondikes Kasino The Game
    time.sleep(0.9)
    print(credit["credit6"]) #     -SnowMan Games
    time.sleep(1.5)
    input("\nPress Enter to Return")
    clear()
