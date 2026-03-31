import os
import gc
from REP.Modules.NPCs.Azure import intro_talk

def clear():
    os.system('cls' if os.name == "nt" else 'clear')
    

shop_items = {
    "Colored_Rod": {"tag": "ocean", "price": 600, "desc": "comes in many different colors", "id": 1},
    "Efficient_Rod": {"tag": "ocean", "price": 800, "desc": "Great rod. good for fishing at the beach", "id": 2},
    "Superior_Rod": {"tag": "ocean", "price": 1200, "desc": "One of the best rods to wield. I bet you will be catching great fish at the beach", "id": 3},
    "Premier_Rod": {"tag": "ocean", "price": 2000, "desc": "The best rod. His name is Rodney.", "id": 4},
    "Basic_lure": {"tag": "lure", "price": 400, "desc": "", "id": 1}, #TODO DESC
    "Scented_lure": {"tag": "lure", "price": 700, "desc": "", "id": 2},
    "Superior_lure": {"tag": "lure", "price": 1000,"desc": "", "id": 3},
    "Magic_Worm": {"tag": "lure", "price": 1500, "desc": "", "id": 4},
}    

class Shop_Ocean:
    __slots__ = ["cd"]

    def __init__(self):
        self.cd: dict = {}
    
    def item_display_function(self, item, price): 
        print()
        
    def main_shop(self, tag, data, lore):

     """for k, v in shop.items(): #grabs item, and item info for each item in shop dict
            if v.get("tag") == tag: # checks if they are in the tag selected
                if not v.get("phase") or v.get("phase") == data["phase"]: # makes sure you in the correct phase if its there (ie furniture.) so it doesnt add ALL furniture to the list.
                    item_display: str = k.replace("_", " ")
                    if k not in items:
                        items.append(k) # appends item to items list for later selection
                    print(f"{shop[k].get("id")}. - {item_display}") # print items
                    time.sleep(self.cd["list_timing"])
                print(lore["shop11"]) # 0. Return"""

        #for k, v in shop_items.items():
            

    def shop_init(self, data: dict, lore: dict, cd: dict):
        if not data["has_met_azure"]:
            intro_talk(cd, data)

        self.cd = cd

