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
                with open(filepath, "r") as game_state:
                    return json.load(game_state)

        except Exception as e:
            return e
    else:
        try:
            with open(filepath, "r") as game_state:
                return json.load(game_state)
        except Exception as e:
            return e

def load_json(file):
    file_path = os.path.join( "REP",JSON_DIR, file)
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except Exception as a:
        return a