#dec 1, start choices :)
from REP.Modules.Saves.save_module import delete_save
import REP.Modules.Saves.Load_module as load
from REP.core.Hub import World

from colorama import Fore, Style, init
import time
import os
game = World

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def select_save(slot):
    if slot in [1, 2, 3]:
        print(f"loading save {slot}")
        time.sleep(1.4)
        game_state = load.load_game(slot)
        return game_state
    else:
        return "nu-uh-uh"
        




init(autoreset=True)
def save_select():
    while True:
        clear_console()
        for idx, i in enumerate(range(3), start=1):
            print(Fore.YELLOW + f"{idx}. Save Slot {i}")
        print("Select Save: ")
        choice = input("> ").strip()

        if choice:
            print("1. load save\n2. Delete save\n3. Go Back")
            save_selected = input("> ").strip()
            if save_selected == "1":
                game_state = select_save(int(choice))
                if game_state != "nu-uh-uh":
                    game.intro(game ,game_state, choice)
                    break
                else:
                    continue
            
            elif save_selected == "2":
                delete_save(int(choice))
                clear_console()
                continue
            elif save_select == "3":
                return
            else:
                clear_console()
                continue
        else:
            clear_console()
            return