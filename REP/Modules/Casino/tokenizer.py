import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def token_shop(lore, Data):
    while True:
        print(lore["token1"])# Welcome to the Tokenizer

        lore7 = lore["token7"].replace('*', Data["c_name"])
        lore8 = lore["token8"].replace("*", Data["c_name"])

        print(lore7)# 1. {c_name} to Tokens
        print(lore8)# 2. Tokens to {c_name}
        print(lore["token9"])# 3. return to Casino hub

        choice = input().strip()# Which exchanger?

        if choice == "3":
            return

        elif choice == "1":
    
            token2 = lore["token2"].replace("*", Data["c_name"])
        
            print(token2)#the exchange rate is 5 {c_name} to 1 token
            print(f"Currency: {Data["currency"]}") # Currency: {currency}
            try:
                token_amount = int(input("> "))
            except ValueError:
                clear()
                print(lore["token6"])
                continue

            if token_amount * 5 > Data["currency"]:
                clear()
                print(lore["token3"])# you dont have enough
                continue
            else:
                token5 = lore["token5"].replace("*", token_amount)
                clear()
                print(lore["token4"]) #okie dokie. let me set you up with the tokens
                Data["currency"] = Data["currency"] - token_amount * 5
                Data["tokens"] = Data["tokens"] + token_amount
                print(token5) # there we go, there is your * tokens. Have fun!
                return

        elif choice == "2:": #tokens to money.
            print(token2)
            print(f"Tokens: {Data["tokens"]}")

            try:
                cash_amount = int(input("> "))
            except ValueError:
                clear()
                print(lore["token6"])
                continue

            if cash_amount % 5 != 0:
                clear() 
                print()# uhhh, this...doesnt...isnt an amount i can convert...    
                continue()

            if cash_amount > Data["tokens"] * 5:
                clear()
                print(lore["token3"])# you dont have enough
                continue
            else:
                print() # Thanks for the tokens, i'll go get the {c_name}
                Data["tokens"] = Data["tokens"] - cash_amount / 5
                Data["currency"] = Data["currency"] + cash_amount
                print()# There ya go! Try not to spend it all in one place...or do. im not your parent.