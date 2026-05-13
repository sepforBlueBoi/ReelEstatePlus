import gc
import random
import time
import sys
from colorama import Fore, Style
from REP.Modules.Casino.roulette import rouletete
from REP.Modules.Casino.tokenizer import token_shop
from REP.Modules.Casino.Slots import slot_animation

def clear() -> None:
    sys.stdout.write("\033[H\033[2J\033[3J")

def slots(Data: dict, text: dict[str, str], cd: dict[str, float]) -> None:
    sys.stdout.write(f'\033]0;Slots\a')
    sys.stdout.flush()
    print(text["slots1"]) # You go to the closest Slots machine.
    time.sleep(cd["text_timing"])

    while True:
        print(text["slots2"]) # The lever becons deaply. 
        time.sleep(cd["text_timing"])
        print(f"Tokens in Pocket: {Data["tokens"]}") # tokens
        time.sleep(cd["text_timing"])
        try:
            amount: int = int(input(text["slots3"])) # How many tokens to you insert into the hole? (Put 0 to return) \n
        except ValueError:
            clear()
            print(text["slots4"]) # the machine refuses whatever you just put in the machine.
            time.sleep(cd["text_timing"])
            continue

        if amount == 0:
            clear()
            print(text["slots5"]) # you leave the machine and return to the casino hub.
            time.sleep(cd["read_timer"])
            clear()
            gc.collect()
            return

        if amount >= 100:
            amount = 99
            print(text["slots9"]) #Sadly the machine will only let you insert 99. Anything else gets returned.
            time.sleep(cd["read_timer"])
            
        if amount < 0:
            print(text["slots10"]) # The Lever wont move without any tokens.
            continue 
        
        if amount > Data["tokens"]:
            print(text["slots11"]) # You do not have that many tokens. 
            continue
            


        time.sleep(cd["text_timing"])
        reel: list[str] = slot_animation() # plays slot animation

        time.sleep(cd["text_timing"])
        clear()
        print(f"   _    _    _")
        print(f" | {reel[0]} | {reel[1]} | {reel[2]} | ,") # prints a sick slot machine
        print(" |              |/")
        time.sleep(cd["text_timing"])

        if reel[0] == reel[1] and reel[1] == reel[2]: # checks for jackpot
            print(text["slots6"])# JACKPOT!
            Data["tokens"] += amount * 2
            time.sleep(cd["text_timer"])

            jackpot: str = str(amount * 2)

            slots7: str = text["slots7"].replace('*', jackpot)

            print(slots7) # You won {amount * 2}!
            time.sleep(cd["read_timer"])
            clear()
            continue

        elif reel[0] == reel[1] or reel[0] == reel[2] or reel[1] == reel[2]: # checks for any match at all
            Data["tokens"] += amount

            win: str = str(amount)
            slots7_5 = text["slots7.5"].replace('*', win)

            print(slots7_5) #You won {amount}!
            time.sleep(cd["read_timer"])
            clear()
            continue
        
        else: # oof
            Data["tokens"] -= amount

            anoumt: str = str(amount)
            slots8_5 = text["slots8.5"].replace('*', anoumt)

            print(text["slots8"]) # Luck was not on your side this roll
            time.sleep(cd["text_timing"])
            print(slots8_5)# You lost {amount}
            time.sleep(cd["read_timer"])
            clear()
            continue

def roulette(Data: dict, text: dict[str, str], cd: dict[str, float]) -> None:
    sys.stdout.write(f'\033]0;Roulette\a')
    sys.stdout.flush()

    print(text["roulette1"])# you walk over to the Roulette table.
    time.sleep(cd["text_timing"])
    color_choice: int = 100 # set here so pyright stops screaming at me. >:(
    while True:
        
        print(text["roulette2.5"] if random.randint(1, 50) == 5 else text["roulette2"])# the ghost manning it greets you asks
        time.sleep(cd["text_timing"])
        roulette1 = text["roulette3"].replace("Red", f"{Fore.RED}Red{Style.RESET_ALL}")
        roulette2 = text["roulette4"].replace("Black", f"{Fore.LIGHTBLACK_EX}Black{Style.RESET_ALL}")
        roulette3 = text["roulette5"].replace("Blue", f"{Fore.BLUE}Blue{Style.RESET_ALL}")
        roulette_purple = text["roulette16"].replace("purple", f"{Fore.MAGENTA}purple{Style.RESET_ALL}")

        print(roulette1)
        time.sleep(cd["list_timing"])
        print(roulette2)
        time.sleep(cd["list_timing"])
        print(roulette3)
        time.sleep(cd["text_timing"])
        print(text["roulette6"])
        time.sleep(cd["text_timing"])


        try:
            color_choice: int = int(input('> '))
        except ValueError:
            clear()
            print(text["roulette17"])
            time.sleep(cd["text_timing"])
            continue

        if color_choice == 1:
            clear()
            color: str = "red"
            
        elif color_choice == 2:
            clear()
            color: str = "black"
            
        elif color_choice == 3:
            clear()
            color: str = "blue"
            
        elif color_choice == 0:
            clear()
            print() # You depart from the table, back to the casinos hub
            gc.collect()
            clear()
            return
        else:
            clear()
            print(roulette_purple)
            continue

        while True:
        
            print(text["roulette7"])# Now the bet.
            time.sleep(cd["text_timing"])
            print(text["roulette8"])# how much you bettin?
            time.sleep(cd["text_timing"])
            print(f"Currency: {Data["currency"]}")# in your wallet is {money}.
            time.sleep(cd["text_timing"])
            print(text["roulette0"]) # Type 0 to return to colors
            try:
                bet: int = int(input("> "))
            except ValueError:
                clear()
                print(text["roulette9"]) # this...isn't an amount
                time.sleep(cd["read_timer"])
                clear()
                continue
        

            roulette6 = text["roulette10"].replace("*", Data["c_name"])
            roulette7 = text["roulette11"].replace("*", Data["c_name"])

            if bet == 0:
                clear()
                print(text["roulette15"])#ah, changing colors?
                time.sleep(cd["read_timer"])
                clear()
                break
        
            if bet <= 19:
                clear()
                print(roulette6)# our lowest bet is 20 {money name}
                time.sleep(cd["read_timer"])
                continue
            elif bet > Data["currency"]:
                clear()
                print(text["roulette12"])# you dont have that much
                time.sleep(cd["read_timer"])
                continue
            elif bet >= 1000:
                clear()
                print(roulette7)# sorry bud, max bet is 999 {money name}
                time.sleep(cd["read_timer"])
                continue
        

            animation_n_result = rouletete()
            time.sleep(cd["text_timing"])
            if color == animation_n_result:
                print(text["roulette13"])# nice win
                time.sleep(cd["text_timing"])
                Data["currency"] += bet
                print(Data["currency"],"!")
                time.sleep(cd["read_timer"])
                gc.collect()
                clear()
                continue
            else:
                print(text["roulette14"])# oof, better luck next time!
                time.sleep(cd["text_timing"])
                Data["currency"] -= bet
                print(Data["currency"],"...")
                time.sleep(cd["read_timer"])
                clear()
                break
        

def Casino(Data: dict, text: dict[str, str], cd: dict[str, float]) -> None:
    sys.stdout.write(f'\033]0;Kasino\a')
    sys.stdout.flush()

    print(text["casino1"])# You enter the imfamous Casino
    time.sleep(cd["text_timing"])
    print(text["casino2"])# Kondike's Kasino...
    time.sleep(cd["text_timing"])
    print(text["casino3"])# The place is ran by ghosts.
    time.sleep(cd["text_timing"])
    while True:
        print(text["casino4"])# Which spot to waste time at first?
        time.sleep(cd["text_timing"])
        print(text["casino5"])# 1. Roulette\n2. Slots?
        time.sleep(cd["text_timing"])
        choice:str = input("> ").lower().strip()

        if choice == "1" or choice == "roulette":
            clear()
            roulette(Data, text, cd)
        elif choice == "2" or choice == "slots":
            clear()
            slots(Data, text, cd)
        elif choice == "3" or choice == "tokens":
            clear()
            token_shop(text, Data, cd)
        elif choice == "0" or choice == "leave":
            clear()
            print(text["casino6"])
            time.sleep(cd["text_timing"])
            print(text["casino7"])
            time.sleep(cd["read_timer"])
            gc.collect()
            clear()
            return
        else:
            print("Try again bozo")
            continue
