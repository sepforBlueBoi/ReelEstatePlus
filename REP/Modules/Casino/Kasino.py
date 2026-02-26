import os
import random
import time
from colorama import Fore, Style, init
from REP.Modules.Casino.roulette import rouletete
from REP.Modules.Casino.tokenizer import token_shop
from REP.Modules.Casino.Slots import slot_animation

def clear():
    os.system('cls' if os.name == "nt" else "clear")

def slots(Data, text, cd):
    print(text["slots1"]) # You go to the closest Slots machine.
    time.sleep(1.4)

    while True:
        print(text["slots2"]) # The lever becons deaply. 
        time.sleep(cd["text_timing"])
        print(f"Tokens in Pocket: {Data["tokens"]}") # tokens
        time.sleep(cd["text_timing"])
        try:
            amount = int(input(text["slots3"])) # How many tokens to you insert into the hole? (Put 0 to return) \n
        except ValueError:
            clear()
            print(text["slots4"]) # the machine refuses whatever you just put in the machine.
            time.sleep(cd["text_timing"])
            continue

        if amount == 0:
            clear()
            print(text["slots5"]) # you leave the machine and return to the casino hub.
            time.sleep(cd["read_timer"])
            return

        if amount >= 100:
            amount = 99
            print(text["slots9"]) #Sadly the machine will only let you insert 99. Anything else gets returned.
            time.sleep(cd["read_timer"])
            
        if amount < 0:
            continue # TODO print statement presumably. plz.
        
        if amount > Data["tokens"]:
            continue # TODO ADD A PRINT STATEMENT HERE TOO >:(
            


        time.sleep(cd["text_timing"])
        reel = slot_animation() # plays slot animation

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

            jackpot = str(amount * 2)

            slots7 = text["slots7"].replace('*', jackpot)

            print(slots7) # You won {amount * 2}!
            time.sleep(cd["read_timer"])
            clear()
            continue

        elif reel[0] == reel[1] or reel[0] == reel[2] or reel[1] == reel[2]: # checks for any match at all
            Data["tokens"] += amount

            win = str(amount)
            slots7_5 = text["slots7.5"].replace('*', win)

            print(slots7_5) #You won {amount}!
            time.sleep(cd["read_timer"])
            clear()
            continue
        
        else: # oof
            Data["tokens"] -= amount

            anoumt = str(amount)
            slots8_5 = text["slots8.5"].replace('*', anoumt)

            print(text["slots8"]) # Luck was not on your side this roll
            time.sleep(cd["text_timing"])
            print(slots8_5)# You lost {amount}
            time.sleep(cd["read_timer"])
            clear()
            continue

def roulette(Data, text, cd):

    print(text["roulette1"])# you walk over to the Roulette table.
    time.sleep(cd["text_timing"])
    while True:
        
        print(text["roulette2.5"] if random.randint(1, 50) == 5 else text["roulette2"])# the ghost manning it greets you asks
        time.sleep(cd["text_timing"])
        roulette1 = text["roulette3"].replace("Red", f"{Fore.RED}Red{Style.RESET_ALL}")
        roulette2 = roulette1.replace("Black", f"{Fore.BLACK}{Style.BRIGHT}Black{Style.RESET_ALL}")
        roulette3 = roulette2.replace("Blue", f"{Fore.BLUE}Blue{Style.RESET_ALL}")
        print(roulette3)# 1. Red 2. Black 3. Blue
        roull = input('> ').strip()

        if roull == "1":
            clear()
            p_color = "red"
            
        elif roull == "2":
            clear()
            p_color = "black"
            
        elif roull == "3":
            clear()
            p_color = "blue"
            
        elif roull == "4":
            clear()
            return
        else:
            clear()
            print(f"No, you cannot bet on {Fore.MAGENTA}purple{Style.RESET_ALL}")
            continue

        while True:
        
            print(text["roulette4"])# Now the bet.
            time.sleep(cd["text_timing"])
            print(text["roulette5"])# how much you bettin?
            time.sleep(cd["text_timing"])
            print(f"Currency: {Data["currency"]}")# in your wallet is {money}.
            time.sleep(cd["text_timing"])
            print(text["roulette0"]) # Type 0 to return to colors
            try:
                bet = int(input("> "))
            except ValueError:
                clear()
                print(text["roulette5.5"]) # this...isn't an amount
                time.sleep(cd["read_timer"])
                clear()
                continue
        

            roulette6 = text["roulette6"].replace("*", Data["c_name"])
            roulette7 = text["roulette7"].replace("*", Data["c_name"])

            if bet == 0:
                clear()
                print(text["roulettereturn"])#ah, changing colors?
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
                print(text["roulette8"])# you dont have that much
                time.sleep(cd["read_timer"])
                continue
            elif bet >= 1000:
                clear()
                print(roulette7)# sorry bud, max bet is 999 {money name}
                time.sleep(cd["read_timer"])
                continue
        

            wow = rouletete()
            time.sleep(cd["text_timing"])
            if p_color == wow:
                print(text["roulette9"])# nice win
                time.sleep(cd["text_timing"])
                Data["currency"] = Data["currency"] + bet
                print(Data["currency"],"!")
                time.sleep(cd["text_timing"])
                input("Press Enter to Continue")
                clear()
                continue
            else:
                print(text["roulette10"])# oof, better luck next time!
                time.sleep(cd["text_timing"])
                Data["currency"] = Data["currency"] - bet
                print(Data["currency"],"...")
                time.sleep(cd["text_timing"])
                input("press Enter to Continue")
                clear()
                break
        

def Casino(Data, text, cd):
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
        choice = input("> ").lower().strip()

        if choice == "1" or choice == "roulette":
            clear()
            roulette(Data, text, cd)
        elif choice == "2" or choice == "slots":
            clear()
            slots(Data, text, cd)
        elif choice == "3" or choice == "tokens":
            clear()
            token_shop(text, Data, cd)
        elif choice == "4" or choice == "leave":
            clear()
            print(text["casino6"])
            time.sleep(cd["text_timing"])
            print(text["casino7"])
            time.sleep(cd["read_timer"])
            clear()
            return
        else:
            print("Try again bozo")
            continue