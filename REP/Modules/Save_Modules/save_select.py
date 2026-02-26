#dec 1, start choices :)
from REP.Modules.Save_Modules.save_module import delete_save
import REP.Modules.Save_Modules.Load_module as load
from REP.core.Hub import World
from colorama import Fore, Style, init
import time
import gc
import os

game = World

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def select_save(slot):
    """_summary_

    Args:
        slot (_type_): _description_

    Returns:
        _type_: _description_
    """
    if slot in [1, 2, 3]: # if it can load
        print(f"loading save {slot}")
        time.sleep(1.4)
        game_state = load.load_game(slot) # load
        gc.set_threshold(700, 10, 10)
        gc.collect(2)
        game.intro(game, game_state, slot)
        
    else:
        return "nu-uh-uh" # NU UH
        




init(autoreset=True)
def save_select():
    """_summary_

    Returns:
        _type_: _description_
    """
    while True:
        clear_console()
        for idx, i in enumerate(range(3), start=1): # prints save slot choices for me
            print(Fore.YELLOW + f"{idx}. Save Slot {i}")
        print("Select Save: ")
        choice = input("> ").strip() # grab the save you want

        if choice:
            print("1. load save\n2. Delete save\n3. Go Back")
            save_selected = input("> ").strip()
            if save_selected == "1":
                select_save(int(choice)) # enters the phase where it may be able to load it
                
            
            elif save_selected == "2":
                delete_save(int(choice))
                print(f"Deleted save {choice}") # kills the save >:)
                time.sleep(3.5)
                clear_console()
                continue
            elif save_select == "3":
                return # leave loop
            else:
                clear_console()
                continue # redo loop if choice wasnt a correct option
        else:
            clear_console()
            continue # loops if no choice