from REP.Modules.Save_Modules.Load_module import load_json
from REP.Modules.Save_Modules.save_module import save_game
from REP.Modules.Casino.Kasino import Casino
from REP.Modules.Checkers.Intro_Checker import *
from REP.Modules.Save_Modules.SaveExit import leaving
from REP.Modules.Misc.Dev_stuff import Terminal
from REP.Modules.Inventory.InvModule import InvDisplay
from REP.Modules.Shop.REP_Shop import Shop
from colorama import Fore, init, Style
import time
import sys, os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear' )

Inv = InvDisplay()
Shop_ = Shop()

class World:
    def __init__(self):
        self.slot = ""
        self.Worldstate = {}
        self.dialogue = {}
        self.timer = {}

    def choice_call(self, choice): # after maing your choice it sends you off.
        clear_console()
        name = self.Worldstate["name"].strip().lower()

        if choice == "1":
            Casino(self.Worldstate, self.dialogue, self.timer)
        elif choice == "2":
            Shop_.shop_init(self.Worldstate, self.dialogue, self.timer)
        elif choice == "3":
            print("lake") #TODO
        elif choice == "4":
            Inv.display(self.Worldstate, self.timer)
        elif choice == "0":
            leaving(self.slot, self.Worldstate, self.dialogue, self.timer)
        elif choice == "{/}" and name == "kondike":
            Terminal(self.Worldstate, self.slot, self.dialogue)
        else:
            clear_console()
            print(self.dialogue["place7"])
        

    def choice(self):
        """choice :)"""
        save_game(self.Worldstate, self.slot) # saves game after intro, and upon opening save
        name = self.Worldstate["name"].strip().lower()
        print(self.dialogue["where1"])
        time.sleep(self.timer["text_timing"])
        print(self.dialogue["where2"] if self.Worldstate["map"] == "owned" else self.dialogue["where2.5"])
        time.sleep(self.timer["text_timing"])
        while True:
            print(self.dialogue["where3"])
            time.sleep(self.timer["text_timing"])
            for x in range(20):
                print("=", end='')
                time.sleep(0.1)
            print("\n")
            print(self.dialogue["place1"] if self.Worldstate["map"] == "owned" else "1. ???") #only prints the name of the place if you own the map offered in intro
            time.sleep(self.timer["list_timing"])
            print(self.dialogue["place2"] if self.Worldstate["map"] == "owned" else "2. ???")
            time.sleep(self.timer["list_timing"])
            print(self.dialogue["place3"] if self.Worldstate["map"] == "owned" else "3. ???")
            time.sleep(self.timer["list_timing"])
            print(self.dialogue["place4"])
            time.sleep(self.timer["list_timing"])
            print(self.dialogue["place5"])
            time.sleep(self.timer["list_timing"])
            if name == "kondike":
                print(self.dialogue["place6"])

            time.sleep(self.timer["list_timing"])
            where_to_go = input("> ") # sick variable name

            self.choice_call(self, where_to_go) # sends you off
        

    def intro(self, save, slot): # intro for post game initialization
        self.slot = slot
        self.dialogue = load_json(file="lore.json")
        self.timer = load_json(file="Global.json")
        self.Worldstate = save
        clear_console()
        if not self.Worldstate["intro"]: # why isnt it working?? hmm
            print(self.dialogue["lore1"])
            for x in range(3):
                print(".", end=' ', flush=True)
                time.sleep(0.7)
            print(self.dialogue["lore2"])
            time.sleep(self.timer["text_timing"])

            Red_you1 = self.dialogue["lore3"].replace("You", f"{Fore.RED}You{Style.RESET_ALL}") # < makes all the "You"s red.
            Red_you2 = self.dialogue["lore4"].replace("You", f"{Fore.RED}You{Style.RESET_ALL}")
            Red_you3 = self.dialogue["lore6"].replace("You", f"{Fore.RED}You{Style.RESET_ALL}")
            Red_you4 = self.dialogue["lore8"].replace("You", f"{Fore.RED}You{Style.RESET_ALL}")

            print(Red_you1) # I don't remember You? [<- red you]
            time.sleep(self.timer["text_timing"])
            while True:
                print(Red_you2) # who are you again?
                name = input("> ")
                smash = name_checker(name)
                if smash == "try again":
                    clear_console()
                    print(self.dialogue["lore5"])
                    continue
                elif smash == "banished":
                    sys.exit() # gone bcause ur name is gaster
                else:
                    response = epic_name_checker(name) # for easter eggs
                    time.sleep(self.timer["text_timing"])
                    print(response) 
                    self.Worldstate["name"] = name
                    time.sleep(self.timer["read_timer"])
                    clear_console()
                    break

            while True:
                print(Red_you3) 
                currency_name = input("> ") # setting currency name
                c_name = money_n_checker(currency_name)
                if c_name == "try again":
                    clear_console()
                    print(self.dialogue["lore5"])
                    continue
                else:
                    self.Worldstate["c_name"] = currency_name
                    time.sleep(self.timer["text_timing"])
                    print(self.dialogue["lore7"])
                    time.sleep(self.timer["read_timer"])
                    clear_console()
                    break

            print(Red_you4)
            time.sleep(self.timer["text_timing"])
            map = input("(Y/N)> ").lower() # check for map
            if map in ["yes", "y"]:
                print(self.dialogue["lore9"]) 
                self.Worldstate["map"] = "owned"
            else:
                print(self.dialogue["lore10"])    
                
            time.sleep(self.timer["text_timing"])
            self.Worldstate["intro"] = True
        clear_console()
        self.choice(self) # enter main game loop