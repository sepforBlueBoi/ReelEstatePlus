#save load
import json
import random
import os


SAVE_DIR = "saves"
os.makedirs(SAVE_DIR, exist_ok=True)
active_slot = 0

save_speech = ["saved", "Saved", "Json File Updated", "Data Uploaded", "Json File consumed", "Backup Made"]

saved = random.choice(save_speech)

def save_game(data, slot): #saves current status to current save slot, aka currect save file
    filepath = os.path.join(SAVE_DIR, f"save_slot_{slot}.json")
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
        print(saved)
    



def delete_save(slot):
    filepath = os.path.join(SAVE_DIR, f"save_slot_{slot}.json")
    if os.path.exists(filepath):
        os.remove(filepath)

        
        