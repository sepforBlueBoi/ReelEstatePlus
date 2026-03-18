from REP.Modules.Fishing.fish_game import Fishing
import os
import time, gc

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

lake = Fishing() 

def checking(data, lore, cd):
    
    has_rod = False
    
    for k, v in data["lake"].items():
        if v:
            has_rod = True
            
    if has_rod and data["equipped_rod"] != None and data["equipped_rod"] in data["lake"]:
        while True:
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(cd["list_timing"])
            print("CAUGHT!")
            time.sleep(cd["text_timing"])
            clear()
            lake.game(data, lore, cd)
            
            time.sleep(cd["text_timing"])
            print(lore["lake12"]) # Fish again?
            choice:str = input("(Y/N)>").lower().strip() 
            gc.collect()
            
            if choice == "y":
                time.sleep(cd["text_timing"])
                
                clear()
                continue
            if choice == "n":
                time.sleep(cd["text_timing"])
                clear()
                print(lore["lake8"]) # what ever floats your boat
                time.sleep(cd["read_timer"])
                clear()
                break
    else:
        clear()
        print(lore["lake9"]) # You have no rods to fish with. go buy one from spamee'o'jr.
        time.sleep(cd["read_timer"])
        clear()
        return