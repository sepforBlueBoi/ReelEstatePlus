#choice anylysis. :P
#class? we'll see.
from REP.Modules.Saves.save_select import save_select
from REP.Modules.Misc.Credits import credits
import os
# custom stall function to KDL, for place holders, simple and ez to undo. no need to redo the same print function over and over
"""PLAN: have a analysis function that checks choice, calls function based off choice. no need for class, not yet, not for this

function: analysis. ran with choice. checks, calls. custom errors? not unless KDL version rigging, but then we have a copy.

i wrote this just to stall...lul. lets do this"""
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def analysis():
    
        
    dec = input("where to look? ")
    if dec == "1": #start game
        clear_console()
        save_select()
        

    
    elif dec == "2":
        clear_console()
        credits()
    
    elif dec == "3":
        clear_console() #TODO Settings
        print("Option 3")

    elif dec == "4":
        clear_console #DLC. not confirmed (confirmed?)
        print("Option 4")

    else:
        clear_console
        print("Not an option.")
            
        
