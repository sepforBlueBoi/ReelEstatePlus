import os
import sys
from REP.Modules.Save_Modules.Load_module import load_json
from REP.Modules.Casino.tokenizer import token_shop
from REP.Modules.Casino.Kasino import slots, roulette, Casino

def clear():
    os.system('cls' if os.name == "nt" else "clear")

places = {
    "place1":{
        "Place_ID": "01",
        "pdesc": "Casino hub"
    },
    "place2":{
        "Place_ID": "02",
        "pdesc": "Slots Machine"
    },
    "place3": {
        "Place_ID": "03",
        "pdesc": "Roulette Table"
    },
    "place4": {
        "Place_ID": "04",
        "pdesc": "Tokenizer Store thing"
    }
}

def backdoor(data, text):
    while True:
        for i in places:
            print(places[i].get("Place_ID"), " - ", places[i].get("pdesc"))
    
        print("Type the Place ID to go there.")
        print("Type return to return")
        plae = input("> ").lower().strip()

        if plae == "return":
            return
    
        if plae == "01":
            clear()
            Casino(data, text)

        if plae == "02":
            clear()
            slots(data, text)   
        
        if plae == "03":
            clear()
            roulette(data, text) 
        
        if plae == "04":
            clear()
            token_shop(text, data)

def Terminal(data, slot, text):

    commands = load_json(file="Cmds.json")
    print("Dev_Terminal Active")
    print("Type -h for more info")

    while True:
        
        cmd = input(f"{data["name"]}@ReelEstate\n>>> ").lower().strip()


        if cmd == "-h":
            print("Type 'Return' to return to the Game")
            print("Type 'ls' to list all the commands")
            print("Type the ID No. of a command to use it")

        if cmd == "ls":
            for i in commands:
                print(commands[i].get("ID") + " - " + commands[i].get("desc"))

        if cmd == "return":
            clear()
            return

        if cmd == "01":
            print("What amount do you want?")
            try:
                amount = int(input("> "))
            except ValueError:
                print("ValueError")
                continue

            data["currency"] = amount
            print(data["currency"])

        if cmd == "02":
            print("What amount do you want?")
            try:
                amount = int(input("> "))
            except ValueError:
                print("ValueError")
                continue

            data["tokens"] = amount
            print(data["tokens"])
            
        if cmd == "04":
            print("Current Currency name to:")
            new_name = input("> ")
            
            if new_name == "":
                print("NameError:Name cannot be empty")
                continue
            
            data["currency_name"] = new_name
            print(f"Currency name changed to: {data['currency_name']}")
            
        if cmd == "05":
            print("Change User name to:")
            new_name = input("> ")
            
            if new_name == "":
                print("NameError:Name cannot be empty")
                continue
            
            data["name"] = new_name
            print(f"User name changed to: {data['name']}")
            
        if cmd == "03":
            clear()
            backdoor(data, text)