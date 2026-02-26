import os, sys
from colorama import Fore, Style, init
import time
from REP.Modules.Save_Modules.save_module import save_game

def clear():
    os.system('cls' if os.name == "nt" else "clear")

def leaving(slot, Data, text, cd):
    """_summary_

    Args:
        slot (_type_): _description_
        Data (_type_): _description_
        text (_type_): _description_

    Returns:
        _type_: _description_
    """
    clear()

    while True:
        quit1 = text["quit1"].replace('You', f"{Fore.RED}You{Style.RESET_ALL}")
        quit2 = text["quit2"].replace('Save', f"{Fore.YELLOW}Save{Style.RESET_ALL}")
        quit5 = text["quit5"].replace('You', f"{Fore.RED}You{Style.RESET_ALL}")
        quit6 = text["quit6"].replace('you', f"{Fore.RED}You{Style.RESET_ALL}")

        print(quit1) # You [<- Red] planning on leaving?
        time.sleep(cd["text_timing"])
        print(quit2) # save // yellow save
        time.sleep(cd["list_timing"])
        print(text["quit3"]) # quit
        time.sleep(cd["list_timing"])
        print(text["quit4"]) # return
        time.sleep(cd["list_timing"])

        choice = input("> ").lower().strip() 
        clear()

        if choice == "3" or choice == "return":
            print(quit5) # You [<- red you] return to the game
            time.sleep(cd["read_timer"])
            clear()
            return

        elif choice == "1" or choice == "save":
            save_game(Data, slot)
            time.sleep(cd["text_timing"])
            continue

        elif choice == "2" or choice == "quit":
            print(quit6) #did you save first?
            save = input("(Y/N)>").lower().strip()

            if save == "n":
                save_game(Data, slot)

            time.sleep(cd["text_timing"])
            print("Cya later alligator!")
            time.sleep(cd["text_timing"])
            sys.exit()
            
        else:
            clear()
            continue
        #TODO ADD A PRINT STATEMENT HEAR YOU A HOLE
        # rude kondike, rude. 

        