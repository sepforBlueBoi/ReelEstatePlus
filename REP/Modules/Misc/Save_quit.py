import os
from colorama import Fore, Style, init
import time
from REP.Modules.Save_Modules.save_module import save_game

def clear():
    os.system('cls' if os.name == "nt" else "clear")

def leaving(slot, Data, text):
    clear()

    quit1 = text["quit1"].replace('You', f"{Fore.RED}You{Style.RESET_ALL}")
    quit2 = text["quit2"].replace('Save', f"{Fore.yellow}Save{Style.RESET_ALL}")
    quit5 = text["quit5"].replace('You', f"{Fore.Red}You{Style.RESET_ALL}")
    quit6 = text["quit6"].replace('you', f"{Fore.Red}You{Style.RESET_ALL}")


    print(quit1) # You [<- Red] planning on leaving?
    time.sleep(1.4)
    print(quit2) # save // yellow save
    time.sleep(0.2)
    print(text["quit3"]) # quit
    time.sleep(0.2)
    print(text[quit4]) # return
    time.sleep(0.2)

    choice = input("> ").lower().strip() 

    if choice == "3" or choice == "return":
        print(quit5) # You [<- red you] return to the game
        time.sleep(3.4)
        return

    if choice == "1" or choice == "save":
        save_game(Data, slot)
        time.sleep(1.4)
        continue

    elif choice == "2" == "quit":
        print(quit6) #did you save first?
        save = input("(Y/N)>").lower().strip()

        if save == "n":
            save_game(Data, slot)

        time.sleep(1.4)
        quit()