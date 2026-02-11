import os
import json
import REP.Modules.Save_Modules.save_module as save
from REP.constants.save_stuff import new_game


SAVE_DIR = "saves"
JSON_DIR = "constants"
os.makedirs(SAVE_DIR, exist_ok=True)

def load_game(slot):
    filepath = os.path.join(SAVE_DIR, f"save_slot_{slot}.json")
    if not os.path.exists(filepath):
        try:
                save.save_game(new_game, slot)  # No save yet
                print("loading...")
                with open(filepath, "r") as game_state: # open it first
                    return json.load(game_state) # return opened file

        except Exception as e: # get error
            return e
    else:
        try:
            with open(filepath, "r") as game_state: # there is a save, so open it
                return json.load(game_state) # then send it off
        except Exception as e:
            return e

def load_json(file):
    file_path = os.path.join( "REP",JSON_DIR, file) # Loads lore.json and etc i guess
    if not os.path.exists(file_path):
        return None # if this happens someone effed up
    try:
        with open(file_path, "r") as f: # open it
            return json.load(f) # send it
    except Exception as a:
        return a