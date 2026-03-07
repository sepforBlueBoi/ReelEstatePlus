from REP.Modules.Fishing.lake import Fishing
import os
import time, gc

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

ocean = Fishing() 

def ocean_game(data: dict, lore: dict, cd: dict):
    has_ocean_rod: bool = False
    
    for k, v in data["ocean"].items():
        if v:
            has_ocean_rod = True
            
    if has_ocean_rod :
        ocean.game(data, lore, cd)