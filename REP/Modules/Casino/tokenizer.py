import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def token_shop(lore, Data):
    print(lore["token1"])# Welcome to the Tokenizer
    while True:
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

