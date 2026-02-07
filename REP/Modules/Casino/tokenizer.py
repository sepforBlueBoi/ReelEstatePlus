import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def token_shop(lore, Data):
    while True:
        print(lore["token1"])# Welcome to the Tokenizer

        lore7 = lore["token7"].replace('*', Data["c_name"])
        lore8 = lore["token8"].replace("*", Data["c_name"])

        time.sleep(1.4)
        print(lore7)# 1. {c_name} to Tokens
        time.sleep(1.4)
        print(lore8)# 2. Tokens to {c_name}
        time.sleep(1.4)
        print(lore["token9"])# 3. return to Casino hub
        time.sleep(1.4)

        choice = input(f"{lore["token13"]} ").strip()# Which exchanger?

        if choice == "3":
            clear()
            print(lore["tokenLeave"]) # You leave the Token shop. You find its weird name to be too weird to use.
            time.sleep(4.5)
            clear()
            return

        elif choice == "1":
            clear()
            token2 = lore["token2"].replace("*", Data["c_name"])
        
            print(token2)#the exchange rate is 5 {c_name} to 1 token
            time.sleep(1.4)
            print(f"Currency: {Data["currency"]}") # Currency: {currency}
            time.sleep(1.4)
            try:
                token_amount = int(input("> "))
            except ValueError:
                clear()
                print(lore["token6"])
                time.sleep(1.4)
                continue

            if token_amount * 5 > Data["currency"]:
                clear()
                print(lore["token3"])# you dont have enough
                time.sleep(1.4)
                continue
            else:
                token_amount_string = str(token_amount)
                token5 = lore["token5"].replace("*", token_amount_string)
                clear()
                print(lore["token4"]) #okie dokie. let me set you up with the tokens
                time.sleep(1.4)
                Data["currency"] = Data["currency"] - token_amount * 5
                Data["tokens"] = Data["tokens"] + token_amount
                print(token5) # there we go, there is your * tokens. Have fun!
                time.sleep(4.5)
                clear()
                continue

        elif choice == "2": #tokens to money.
            clear()
            print(token2)
            time.sleep(1.4)
            print(f"Tokens: {Data["tokens"]}")
            time.sleep(1.4)

            try:
                cash_amount = int(input("> "))
            except ValueError:
                clear()
                print(lore["token6"])
                time.sleep(1.4)
                continue

            if cash_amount % 5 != 0: # this is mean math >:\
                clear() 
                print(lore["token10"])# uhhh, this...doesnt...isnt an amount i can convert...    
                time.sleep(1.4)
                continue

            if cash_amount > Data["tokens"] * 5:
                clear()
                print(lore["token3"])# you dont have enough
                time.sleep(1.4)
                continue
            else:

                token11 = lore["token11"].replace('*', Data["c_name"])

                print(token11) # Thanks for the tokens, i'll go get the {c_name}
                time.sleep(1.4)
                Data["tokens"] = Data["tokens"] - cash_amount / 5
                Data["currency"] = Data["currency"] + cash_amount
                print(lore["token12"])# There ya go! Try not to spend it all in one place...or do. im not your parent.
                time.sleep(3.4)
                clear()
                continue

        else:
            clear()
            print(lore["tokenrant"]) #No. bad. Legit where are you attepting to go. Hey hey, dont ignore my rant, hey...You tune out the narrators rant.
            time.sleep(1.4)
            continue