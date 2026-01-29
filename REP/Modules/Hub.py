import time
from REP.Modules.Saves.Load_module import load_json
from REP.Modules.Saves.save_module import save_game
from REP.Modules.Checkers.Intro_Checker import *
from colorama import Fore, init, Style


class World:
    def init(self):
        self.slot = ""
        self.Worldstate = {}
        self.dialogue = {}

    def choice(self):
        """choice :)"""
        save_game(self.Worldstate, self.slot)
        

    def intro(self, save, slot):
        self.slot = slot
        self.dialogue = load_json(file="lore.json")
        self.Worldstate = save

        if self.Worldstate["intro"] == "False":
            print(self.dialogue["lore1"])
            for x in range(3):
                print(".", end=' ', flush=True)
                time.sleep(0.9)
            print(self.dialogue["lore2"])
            time.sleep(1.2)

            Red_you1 = self.dialogue["lore3"].replace("You", f"{Fore.RED}You{Style.RESET_ALL}")
            Red_you2 = self.dialogue["lore4"].replace("You", f"{Fore.RED}You{Style.RESET_ALL}")
            Red_you3 = self.dialogue["lore6"].replace("You", f"{Fore.RED}You{Style.RESET_ALL}")
            Red_you4 = self.dialogue["lore8"].replace("You", f"{Fore.RED}You{Style.RESET_ALL}")

            print(Red_you1) # I don't remember You? [<- red you]
            while True:
                print(Red_you2) # who are you again?
                name = input("> ")
                smash = name_checker(name)
                if smash == "try again":
                    print(self.dialogue["lore5"])
                    continue
                else:
                    response = epic_name_checker(name)
                    print(response) 
                    self.Worldstate["name"] = name
                    break

            while True:
                print(Red_you3) # well while you're here, what is the currency of this world?
                currency_name = input("> ")
                c_name = money_n_checker(currency_name)
                if c_name == "try again":
                    print(self.dialogue["lore5"])
                    continue
                else:
                    self.Worldstate["c_name"] = currency_name
                    print(self.dialogue["lore7"]) # good enough for a name. okie dokie, you may enter the Town of jahabler!
                    break

            print(Red_you4) # now. i'll ask this ONCE, unlike last time. do you want the map?
            map = input("(Y/N)> ").lower()
            if map in ["yes", "y"]:
                print(self.dialogue["lore9"]) # Amazing. you get this map i just made out of thin air
                self.Worldstate["map"] = "owned"
            else:
                print("Womp Womp")    

        self.Worldstate["intro"] = "Done"
        self.choice(self) 