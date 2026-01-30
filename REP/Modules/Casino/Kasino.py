import os
import random
import time
from colorama import Fore, Style, init
from REP.Modules.Casino.roulette import rouletete
from REP.Modules.Casino.tokenizer import token_shop

def clear():
    os.system('cls' if os.name == "nt" else "clear")

def roulette(Data, text):

    print(text["roulette1"])# you walk over to the Roulette table.
    time.sleep(1.4)
    while True:
        
        print(text["roulette2.5"] if random.randint(1, 50) == 5 else text["roulette2"])# the ghost manning it greets you asks
        time.sleep(1.4)
        roulette1 = text["roulette3"].replace("Red", f"{Fore.RED}Red{Style.RESET_ALL}")
        roulette2 = roulette1.replace("Black", f"{Fore.BLACK}{Style.BRIGHT}Black{Style.RESET_ALL}")
        roulette3 = roulette2.replace("Blue", f"{Fore.BLUE}Blue{Style.RESET_ALL}")
        print(roulette3)# 1. Red 2. Black 3. Blue
        roull = input('> ').strip()

        if roull == "1":
            clear()
            p_color = "red"
            break
        elif roull == "2":
            clear()
            p_color = "black"
            break
        elif roull == "3":
            clear()
            p_color = "blue"
            break
        elif roull == "4":
            clear()
            return
        else:
            clear()
            print(f"No, you cannot bet on {Fore.MAGENTA}purple{Style.RESET_ALL}")
            continue

    while True:
        
        print(text["roulette4"])# Now the bet.
        time.sleep(1.4)
        print(text["roulette5"])# how much you bettin?
        time.sleep(1.4)
        print(f"Currency: {Data["currency"]}")# in your wallet is {money}.
        try:
            bet = int(input("> "))
        except ValueError:
            clear()
            print(text["roulette5.5"]) # this...isn't an amount
            continue
        

        roulette6 = text["roulette6"].replace("*", Data["c_name"])
        roulette7 = text["roulette7"].replace("*", Data["c_name"])

        if bet <= 19:
            clear()
            print(roulette6)# our lowest bet is 20 {money name}
            continue
        elif bet > Data["currency"]:
            clear()
            print(text["roulette8"])# you dont have that much
            continue
        elif bet >= 1000:
            clear()
            print(roulette7)# sorry bud, max bet is 999 {money name}
            continue
        else:
            break

    wow = rouletete()
    time.sleep(2)
    if p_color == wow:
        print(text["roulette9"])# nice win
        time.sleep(1.4)
        Data["currency"] = Data["currency"] + bet
        print(Data["currency"],"!")
        time.sleep(1.4)
        input("Press Enter to Continue")
        clear()
    else:
        print(text["roulette10"])# oof, better luck next time!
        time.sleep(1.4)
        Data["currency"] = Data["currency"] - bet
        time.sleep(1.4)
        print(Data["currency"],"...")
        input("press Enter to Continue")
        clear()
        

def Casino(Data, text):
    print(text["casino1"])# You enter the imfamous Casino
    time.sleep(1.4)
    print(text["casino2"])# Kondike's Kasino...
    time.sleep(1.4)
    print(text["casino3"])# The place is ran by ghosts.
    time.sleep(1.4)
    while True:
        print(text["casino4"])# Which spot to waste time at first?
        time.sleep(1.4)
        print(text["casino5"])# 1. Roulette\n2. Slots?
        time.sleep(1.4)
        choice = input("> ").lower().strip()

        if choice == "1" or choice == "roulette":
            clear()
            roulette(Data, text)
        elif choice == "2" or choice == "slots":
            clear()
            print("slots")
        elif choice == "3" or choice == "tokens":
            clear()
            token_shop(text, Data)
        elif choice == "4" or choice == "leave":
            print(text["casino6"])
            time.sleep(1.4)
            print(text["casino7"])
            time.sleep(1.4)
            return
        else:
            print("Try again bozo")
            continue