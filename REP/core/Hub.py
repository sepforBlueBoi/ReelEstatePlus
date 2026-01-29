import time
from REP.Modules.Saves.Load_module import load_json
from REP.Modules.Saves.save_module import save_game
from REP.Modules.Casino.Kasino import Casino
from REP.Modules.Checkers.Intro_Checker import *
import sys, os
from colorama import Fore, init, Style

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear' )

class World:
    def init(self):
        self.slot = ""
        self.Worldstate = {}
        self.dialogue = {}

    def choice_call(self, choice):
        clear_console()
        name = self.Worldstate["name"].strip().lower()

        if choice == "1":
            Casino(self.Worldstate, self.dialogue)
        elif choice == "2":
            print("shop")
        elif choice == "3":
            print("lake")
        elif choice == "4":
            print("Inventory")
        elif choice == "0":
            print("save quit menu")
        elif choice == "{/}" and name == "kondike":
            print("Dev Console")
        

    def choice(self):
        """choice :)"""
        save_game(self.Worldstate, self.slot)
        name = self.Worldstate["name"].strip().lower()
        print(self.dialogue["where1"])
        time.sleep(1.4)
        print(self.dialogue["where2"] if self.Worldstate["map"] == "owned" else self.dialogue["where2.5"])
        while True:
            time.sleep(1.4)
            print(self.dialogue["where3"])
            time.sleep(1.4)
            for x in range(20):
                print("=", end='')
                time.sleep(0.1)
            print("\n")
            print(self.dialogue["place1"] if self.Worldstate["map"] == "owned" else "1. ???")
            time.sleep(0.2)
            print(self.dialogue["place2"] if self.Worldstate["map"] == "owned" else "2. ???")
            time.sleep(0.2)
            print(self.dialogue["place3"] if self.Worldstate["map"] == "owned" else "3. ???")
            time.sleep(0.2)
            print(self.dialogue["place4"])
            time.sleep(0.2)
            print(self.dialogue["place5"])
            time.sleep(0.2)
            if name == "kondike":
                print(self.dialogue["place6"])

            time.sleep(0.2)
            where_to_go = input("> ")

            self.choice_call(self, where_to_go)
        

    def intro(self, save, slot):
        self.slot = slot
        self.dialogue = load_json(file="lore.json")
        self.Worldstate = save
        clear_console()
        if self.Worldstate["intro"] == "False":
            print(self.dialogue["lore1"])
            for x in range(3):
                print(".", end=' ', flush=True)
                time.sleep(0.7)
            print(self.dialogue["lore2"])
            time.sleep(1.2)

            Red_you1 = self.dialogue["lore3"].replace("You", f"{Fore.RED}You{Style.RESET_ALL}")
            Red_you2 = self.dialogue["lore4"].replace("You", f"{Fore.RED}You{Style.RESET_ALL}")
            Red_you3 = self.dialogue["lore6"].replace("You", f"{Fore.RED}You{Style.RESET_ALL}")
            Red_you4 = self.dialogue["lore8"].replace("You", f"{Fore.RED}You{Style.RESET_ALL}")

            print(Red_you1) # I don't remember You? [<- red you]
            time.sleep(1.2)
            while True:
                print(Red_you2) # who are you again?
                name = input("> ")
                smash = name_checker(name)
                if smash == "try again":
                    clear_console()
                    print(self.dialogue["lore5"])
                    continue
                elif smash == "banished":
                    sys.exit()
                else:
                    response = epic_name_checker(name)
                    time.sleep(1.2)
                    print(response) 
                    self.Worldstate["name"] = name
                    time.sleep(4.5)
                    clear_console()
                    break

            while True:
                print(Red_you3) 
                currency_name = input("> ")
                c_name = money_n_checker(currency_name)
                if c_name == "try again":
                    clear_console()
                    print(self.dialogue["lore5"])
                    continue
                else:
                    self.Worldstate["c_name"] = currency_name
                    time.sleep(1.2)
                    print(self.dialogue["lore7"])
                    time.sleep(4.5)
                    clear_console()
                    break

            print(Red_you4)
            time.sleep(1.2)
            map = input("(Y/N)> ").lower()
            if map in ["yes", "y"]:
                print(self.dialogue["lore9"]) 
                self.Worldstate["map"] = "owned"
            else:
                print(self.dialogue["lore10"])    
                
            time.sleep(4.5)
            self.Worldstate["intro"] = "Done"
        clear_console()
        self.choice(self) 