import os, sys
import time, gc
from REP.Modules.Fishing.Ocean.OceanChecker import ocean_game
from REP.Modules.Shop.Ocean_Shop import Shop_Ocean

def clear():
    sys.stdout.write("\033[H\033[2J\033[3J")
    
Azure_cove = Shop_Ocean()
    
def ocean_begans(data: dict, lore: dict, cd: dict):
    print(lore["ocean1"]) # The path to the ocean is overgrown.  
    time.sleep(cd["text_timing"])                          
    print(lore["ocean2"]) # But on the otherside of the forest between here and the town...
    time.sleep(cd["text_timing"])
    print(lore["ocean3"] + '\n') # A beautiful beach lays with a dock.       
    time.sleep(cd["text_timing"])                     
    
    if not data['has_met_azure']:
        print(lore["ocean4"]) # A store sits above the sand, a hand made sign sits out front.
        time.sleep(cd["text_timing"])
        print(lore["ocean5"] + '\n') # it reads 'Azures Cove'
        time.sleep(cd["text_timing"])
    
    while True:
        print(lore["ocean9"] + '\n') # What is this place?
        time.sleep(cd["text_timing"])
        
        print(lore["ocean6"]) # 1. fish
        time.sleep(cd["list_timing"])
        print(lore["ocean7"]) # 2. Beach front store
        time.sleep(cd["list_timing"])
        print(lore["ocean8"] + '\n') # 0. Return
        time.sleep(cd["list_timing"])

        try:
            choice: int = int(input("> "))
        except ValueError:
            print(lore["ocean10"]) # You do some weird dance. the crabs seem scared of you.
            
        if choice == 0:
            clear()
            time.sleep(cd["text_timing"])
            print() # You take the hike back to town.
            time.sleep(cd["read_timer"])
            clear()
            gc.collect()
            return
        elif choice == 1:
            ocean_game(data, lore, cd)
        elif choice == 2:
            Azure_cove.shop_init(data, lore, cd)
        else:
            print(lore["ocean13"]) # The Person in Azures Cove is watching you.
