import os
import sys
from REP.Modules.Save_Modules.Load_module import load_json

def Terminal(data, slot, text):

    commands = load_json(file="Cmds.json")

    while True:
        print("Dev_Terminal Active")
        print("Type -h for more info")

        cmd = input("> ").lower().strip()


        if cmd == "-h":
            print("Type Return to return to the Game")