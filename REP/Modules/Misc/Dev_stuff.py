import os
from REP.Modules.Save_Modules.Load_module import load_json
from REP.Modules.Casino.tokenizer import token_shop # used on line 54
from REP.Modules.Casino.Kasino import slots, roulette, Casino # lines 46, 50, 42 respectivly

def clear(): # clear console
    os.system('cls' if os.name == "nt" else "clear")

places = { # all the accessable places
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
    
    """The 'Back door'. its really just a faster way to go places for testing, being it bypasses all unlocks."""
    
    while True:
        for i in places: # prints every place accessable 
            print(places[i].get("Place_ID"), " - ", places[i].get("pdesc"))
    
        print("Type the Place ID to go there.")
        print("Type return to return")
        plae = input("> ").lower().strip()

        if plae == "return": # return
            return
    
        if plae == "01": # to casino hub
            clear()
            Casino(data, text)

        if plae == "02": # to slots
            clear()
            slots(data, text)   
        
        if plae == "03": # to roulette
            clear()
            roulette(data, text) 
        
        if plae == "04": # to the token shop
            clear()
            token_shop(text, data)

def Terminal(data, slot, text):
    
    """Simple Dev terminal for hacking in, and editing currency. as well as backdoor access. only accessable by naming yourself Kondike
    
    all 5 commands can be found in Cmds.json"""
    
    
    commands = load_json(file="Cmds.json") # loading Cmds.json using load_json from the load module in Save_Modules
    
    print("Dev_Terminal Active")
    print("Type -h for more info")

    while True:
        
        cmd = input(f"{data["name"]}@ReelEstate\n>>> ").lower().strip()

# lines 64-69, ls, and -h commands are to imitate Linux terminal commands

        if cmd == "-h":
            print("Type 'Return' to return to the Game")
            print("Type 'ls' to list all the commands")
            print("Type the ID No. of a command to use it")

        if cmd == "ls":
            for i in commands:
                print(commands[i].get("ID") + " - " + commands[i].get("desc")) # prints commands

        if cmd == "return": # returns to where you came from
            clear()
            return

        if cmd == "01":  # Changes Currency amount
            print("What amount do you want?")
            try:
                amount = int(input("> "))
            except ValueError:
                print("ValueError")
                continue

            data["currency"] = amount
            print(data["currency"])

        if cmd == "02": # Changes token amount
            print("What amount do you want?")
            try:
                amount = int(input("> "))
            except ValueError:
                print("ValueError")
                continue

            data["tokens"] = amount
            print(data["tokens"])
            
        if cmd == "04": # changes currency name
            print("Current Currency name to:")
            new_name = input("> ")
            
            if new_name == "":
                print("NameError:Name cannot be empty")
                continue
            
            data["currency_name"] = new_name
            print(f"Currency name changed to: {data['currency_name']}")
            
        if cmd == "05": # changes player name
            print("Change User name to:")
            new_name = input("> ")
            
            if new_name == "":
                print("NameError:Name cannot be empty")
                continue
            
            data["name"] = new_name
            print(f"User name changed to: {data['name']}")
            
        if cmd == "03": # the back door
            clear()
            backdoor(data, text)