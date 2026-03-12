from REP.Modules.Fishing.fish_game import Fishing
from REP.constants.save_stuff import game_dict
import json
import os

data = game_dict
Fish = Fishing()

JSON_DIR = "constants"
const = "Globals.json"
text = "lore.json"

def load_json(file):
    file_path = os.path.join( "REP",JSON_DIR, file) # Loads lore.json and etc i guess
    if not os.path.exists(file_path):
        return None # if this happens someone effed up
    try:
        with open(file_path, "r") as f: # open it
            return json.load(f) # send it
    except Exception as a:
        return a

def test_fish_gen():
    
    fash = Fish.random_gen(data)
    assert True
    
def test_game_gen():
    Fish.game_gen()
    assert True
    
