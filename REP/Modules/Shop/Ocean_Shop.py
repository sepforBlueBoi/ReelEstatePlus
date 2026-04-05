import os
import gc, sys, time
from REP.Modules.NPCs.Azure import intro_talk

def clear():
    os.system('cls' if os.name == "nt" else 'clear')
    

shop_items = {
    "Colored_Rod": {"tag": "ocean", "price": 600, "desc": "comes in many different colors", "id": 1},
    "Efficient_Rod": {"tag": "ocean", "price": 800, "desc": "Great rod. good for fishing at the beach", "id": 2},
    "Superior_Rod": {"tag": "ocean", "price": 1200, "desc": "One of the best rods to wield. I bet you will be catching great fish at the beach", "id": 3},
    "Premier_Rod": {"tag": "ocean", "price": 2000, "desc": "The best rod. His name is Rodney.", "id": 4},
    "Basic_lure": {"tag": "lures", "price": 400, "desc": "Pretty decent lure.", "id": 1}, 
    "Scented_lure": {"tag": "lures", "price": 700, "desc": "The lure is scented like tide pods. thats what fish like right?", "id": 2},
    "Superior_lure": {"tag": "lures", "price": 1000,"desc": "Much like the rod, it is superior, despite being the second best.", "id": 3},
    "Magic_Worm": {"tag": "lures", "price": 1500, "desc": "Its a worm covered in glitter.", "id": 4},
}    

class Shop_Ocean:
    __slots__ = ["cd"]

    def __init__(self):
        self.cd: dict = {}
    
    def item_display_function(self, item, price): 
        item_view = item.replace("_", " ")
        print(f"o|== ~{item_view}~ ==|o")
        print("\n")
        
        time.sleep(self.cd["text_timing"])
        print(shop_items[item].get("desc"))
        time.sleep(self.cd["text_timing"])

        print(f"${price}")
        time.sleep(self.cd["text_timing"])
        
    def main_shop(self, tag, data, lore):
        items: list[str] = ["placerholder"]

        """for k, v in shop.items(): #grabs item, and item info for each item in shop dict
            if v.get("tag") == tag: # checks if they are in the tag selected
                if not v.get("phase") or v.get("phase") == data["phase"]: # makes sure you in the correct phase if its there (ie furniture.) so it doesnt add ALL furniture to the list.
                    item_display: str = k.replace("_", " ")
                    if k not in items:
                        items.append(k) # appends item to items list for later selection
                    print(f"{shop[k].get("id")}. - {item_display}") # print items
                    time.sleep(self.cd["list_timing"])
                print(lore["shop11"]) # 0. Return"""

        title = ""
        match tag:
            case "ocean":
                title = "Advanced Rods"
            case "lure":
                title = "Fishing Lures"

        while True:
            print("-" * 2, "=" * 3, title, "=" * 3, "-" * 2)

            print('\n')
            for k, v in shop_items.items():
                if v.get("tag") == tag:
                    item_display: str = k.replace("_", " ")
                    if k not in items:
                        items.append(k)
                    print(f"{shop_items[k].get("id")}. | {item_display}")  
            print(lore["shop11"])

            item_choice: int = 10 # another place holder for pyright
    
            try:
                item_choice: int = int(input("> "))
            except ValueError:
                clear()
                print() # [Blue] Please select an item.
                time.sleep(self.cd["read_timer"])
                clear()
                continue

            if item_choice == 0:
                clear()
                print() # You leave this isle. Azure is building a card house from letters.
                time.sleep(self.cd["read_timer"])
                clear()
                return
            
            time.sleep(self.cd["text_timing"])
            price = shop_items[items[item_choice]].get("price")

            while True:
                clear()
                self.item_display_function(items[item_choice], price)

                print("\n")
                print(lore["shop18"] if data[tag].get(items[item_choice]) == False else lore ["shop19"])

                

    def shop_init(self, data: dict, lore: dict, cd: dict):
        if not data["has_met_azure"]:
            intro_talk(cd, data)
            data["has_met_azure"] = True

        self.cd = cd
        sys.stdout.write(f"\033]0;Azure's Cove\a")
        sys.stdout.flush()

        choice = 500
        clear()
        print(lore["ocean_shop1"]) # Despite the narrator leaving, he is still narrating from out side....somehow.
        time.sleep(self.cd["text_timing"])
        while True:
            print(lore["ocean_shop2"]) # Azure is watching me intently from inside
            time.sleep(self.cd["text_timing"])

            print(lore["ocean_shop3"]) # 1. Advanced rods
            time.sleep(self.cd["list_timing"]) 
            print(lore["ocean_shop4"]) # 2. Lures
            time.sleep(self.cd["list_timing"])
            print(lore["ocean_shop5"]) # 4. chat
            time.sleep(self.cd["list_timing"])
            print(lore["ocean_shop6"]) # 0. Leave
            time.sleep(self.cd["list_timing"])
    
            try:
                choice: int = int(input("\n> "))
            except ValueError:
                clear()
                print(lore["ocean_shop7"]) # You walk into the floor
                time.sleep(self.cd["text_timing"])
    
            if choice == 0:
                clear()
                print(lore["ocean_shop8"]) # You leave the cove, back to the sandy beach.
                time.sleep(self.cd["read_timer"])
                clear()
                gc.collect()
                return

            match choice:
                case 1:
                    time.sleep(self.cd["text_timing"])
                    clear()
                    self.main_shop("ocean", data, lore)
                case 2:
                    time.sleep(self.cd["text_timing"])
                    clear()
                    self.main_shop("lures", data, lore)
                case _:
                    time.sleep(self.cd["text_timing"])
                    clear()
                    print(lore["ocean_shop9"]) # Another floor. Please stop walking into stuff.
                    time.sleep(self.cd["text_timing"])
                    continue

