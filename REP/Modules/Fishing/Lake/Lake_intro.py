import os
import time
import random, gc
from REP.Modules.Fishing.Lake.FishingChecker import checking

def clear():
    os.system('cls' if os.name == "nt" else "clear")
    

def lake_init(data, lore, cd): # lake intro wooo. fun.
    """fish intro for reel estate plus."""
    print(lore["lake1"])# You Walk the path to the lake.
    time.sleep(cd["text_timing"])
    print(lore["lake2"]) # Some birds fly over head.
    time.sleep(cd["text_timing"])
    print("\n")
    
    while True:
        print() # What to do?
        time.sleep(cd["text_timing"])
    
        print(lore["lake3"]) # 1. fish
        time.sleep(cd["list_timing"])
        print(lore["lake4"]) # 2. return
        time.sleep(cd["list_timing"])
        print("\n")
    
        try:
            choice:int = int(input("> "))
        except ValueError:
            print(lore["lake5"]) # You still cant climb a tree.
        
        if choice == 1:
            checking(data, lore, cd)
            print() 
        elif choice == 2:
            time.sleep(cd["text_timing"])
            print(lore["lake6"]) #You depart from the edge of the town, returning to the middle of it.
            time.sleep(cd["read_timer"])
            gc.collect()
            clear()
            return
        else:
            time.sleep(cd["text_timing"])
            clear()
            print(lore["lake7"]) # you slip in the mud and roll up a hill.
            time.sleep(cd["text_timing"])
            continue