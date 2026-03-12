#save load
import orjson
import random
import os


SAVE_DIR = "saves"
os.makedirs(SAVE_DIR, exist_ok=True)
active_slot = 0

save_speech = ["saved", "Saved", "Json File Updated", "Data Uploaded", "Json File consumed", "Backup Made"] # printed messages when saved/ing


def save_game(data, slot): #saves current status to current save slot, aka currect save file
    """_summary_

    Args:
        data (_type_): _description_
        slot (_type_): _description_
    """
    saved = random.choice(save_speech)

    filepath = os.path.join(SAVE_DIR, f"save_slot_{slot}.json")
    with open(filepath, "wb") as f: # opens it
        f.write(orjson.dumps(data, option=orjson.OPT_INDENT_2)) # dumps the save data in
        print(saved)
    



def delete_save(slot): # kills the save
    filepath = os.path.join(SAVE_DIR, f"save_slot_{slot}.json")
    if os.path.exists(filepath):
        os.remove(filepath)

        
        