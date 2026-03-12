import os
import orjson
import REP.Modules.Save_Modules.save_module as save
from REP.constants.save_stuff import new_game


SAVE_DIR: str = "saves"
JSON_DIR: str = "constants"
os.makedirs(SAVE_DIR, exist_ok=True)

def load_game(slot):
    """_summary_

    Args:
        slot (_type_): _description_

    Returns:
        _type_: _description_
    """
    filepath = os.path.join(SAVE_DIR, f"save_slot_{slot}.json")
    if not os.path.exists(filepath):
        try:    
                new_save: dict[str, any] = new_game()
                save.save_game(new_save, slot)  # No save yet
                print("loading...")
                with open(filepath, "rb") as game_state: # open it first
                    return orjson.loads(game_state.read()) # return opened file

        except Exception as e: # get error
            return e
    else:
        try:
            with open(filepath, "rb") as game_state: # there is a save, so open it
                return orjson.loads(game_state.read()) # then send it off
        except Exception as e:
            return e

def load_json(file):
    file_path: str = os.path.join( "REP",JSON_DIR, file) # Loads lore.json and etc i guess
    if not os.path.exists(file_path):
        return None # if this happens someone effed up
    try:
        with open(file_path, "rb") as f: # open it
            return orjson.loads(f.read()) # send it
    except Exception as a:
        return a