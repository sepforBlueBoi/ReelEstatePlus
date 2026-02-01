import os
import sys
from REP.Modules.Save_Modules.Load_module import load_json

def clear():
    os.system('cls' if os.name == "nt" else "clear")


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
