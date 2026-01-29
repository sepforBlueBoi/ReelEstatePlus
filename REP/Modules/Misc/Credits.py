import time
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
from REP.Modules.Saves.Load_module import load_json

credit = load_json("lore.json")

def credits():
    print(credit["credit1"]) # Reel Estate+
    time.sleep(0.9)
    print(credit["credit2"]) # Made my Kondike
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