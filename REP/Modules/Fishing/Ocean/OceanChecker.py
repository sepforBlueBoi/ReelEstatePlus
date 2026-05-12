from REP.Modules.Fishing.fish_game import Fishing
import os, sys
import time, gc

def clear():
    sys.stdout.write("\033[H\033[2J\033[3J")

ocean = Fishing() 

def ocean_game(data: dict, lore: dict, cd: dict):

                        
    if data["equipped_rod"] != None:
        while True:
            for i in range(5):
                print(".", end="", flush=True)
                time.sleep(cd["list_timing"])
            print("CAUGHT!!")
            time.sleep(cd["text_timing"])
            clear()
            ocean.game(data, lore, cd)
            
            time.sleep(cd["text_timing"])
            print(lore["ocean11"]) # Cast your rod again?
            choice:str = input("(Y/N)>").lower().strip() 
            gc.collect()
            
            if choice == "y":
                time.sleep(cd["text_timing"])
                
                clear()
                continue
            if choice == "n":
                time.sleep(cd["text_timing"])
                clear()
                print(lore["ocean12"]) # you part from the dock, back to the sand.
                time.sleep(cd["read_timer"])
                clear()
                break
