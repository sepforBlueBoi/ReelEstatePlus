#SHOP
import os
import time
import random

def clear():
    os.system('cls' if os.name == "nt" else "clear")
    
    
class Shop:
    
    def __init__(self):
        self.cd = {}
    
    def item_display_function(self, item, desc, price): # item display logic for polish. 
    
        shop_item = item.replace("_", " ")
        print(f"====={shop_item}=====")
        print("\n")
        time.sleep(self.cd["text_timing"])
    
        print(desc.get("desc"))
        time.sleep(self.cd["text_timing"])
    
        if price != desc.get("price"):
            Price = f"[{desc.get("price")}] -> {price}"
        
        else:
            Price = price
    
        print(f"${Price}")
        time.sleep(self.cd["text_timing"])
    
    def shop(self, tag, data, sale, lore):
        """Display_items = dict(items)
    if category == "houses" and not all(game_state["npcs"].values()):
        display_items = {k: v for k, v in items.items() if k != "kasino"}
    while True:
        print(f" {category.title()} isle")
        for idx, (item_name, data) in enumerate(display_items.items(), start=1):
            item_id = data["id"]
            price = data["price"]
            bought = game_state["bought"].get(item_id, False)
            status = "BOUGHT" if bought else f"${price} {game_state['money']}"
            print(f"{idx}. {item_name} - {status}")
        print(f"{len(display_items)+1}. Leave")
        
    ^ Not important. old logic from Legacy 8.1, used for example to get print items to work
    """
        items = ["placeholder"] # place holder so items start at index 1.
    
        match tag: # grabs the title of the page/isle based off of tag.
            case "house":
                title = "Real Estate"
            case "furniture":
                title = "Furniture"
            case "lake":
                title = "Fishing"
            case "misc":
                title = "Miscellaneous"
            
        while True:
            print("=" * 5, title, "=" * 5)
            if sale != 1.0:
                time.sleep(self.cd["text_timing"])
                print("All items are half price")
        
            time.sleep(self.cd["text_timing"])
            print("\n")
        
            for k, v in data["shop"].items(): #grabs item, and item info for each item in shop dict
                if v.get("tag") == tag: # checks if they are in the tag selected
                    item_display = k.replace("_", " ")
                    if k not in items:
                        items.append(k) # appends item to items list for later selection
                    desc = v
                    print(f"{desc.get("id")}. - {item_display}") # print items
                    time.sleep(self.cd["list_timing"])
            print(lore["shop11"]) # 0. Return
                
            try:
                item = int(input("> "))
            except ValueError:
                clear()
                print(lore["shop15"]) # You hear a loud buzzer blare
                continue
        
            if item == 0:
                clear()
                print(lore["shop16"]) # You leave the isle, the cashier seems bored.
                time.sleep(self.cd["read_timer"])
                clear()
                return
        
            if item > len(items) or item < 0: 
                clear()
                print(lore["shop17"]) # You slip and land face first into a wall. What were you going for?
                time.sleep(self.cd["text_timing"])
                continue
        
            time.sleep(self.cd["text_timing"])
        
            while True:
                price = desc.get("price") * sale
                clear()
                self.item_display_function(items[item], desc, price) # Display item, item descripton, and price.
            
                print()
            
    
    def shop_init(self, data, lore, cd):
        """_summary_

    Args:
        data (_type_): _description_
        lore (_type_): _description_
    """
        self.cd = cd
        
        print(lore["shop1"]) # you walk into the little shop. the bell above the door dings
        time.sleep(self.cd["text_timing"])
        print(lore["shop2"]) # the Cashier greets you.
        time.sleep(self.cd["text_timing"])
        print(lore["shop3"], "\n") # Hello there!
        time.sleep(self.cd["text_timing"])
    
        sales = 1.0
        if random.randint(1, 65) == 1:
            sales = 0.5 #sales :)
    
        while True:
            print(lore["shop4"]) # There are a wide array of isles. 
            time.sleep(self.cd["text_timing"])
            print(lore["shop5"], "\n") # including an isle for houses. sadly It's just the map and keys to the houses.
            time.sleep(self.cd["text_timing"])
       
            print(lore["shop6"]) # 1. Real Estate
            time.sleep(self.cd["list_timing"])
            print(lore["shop7"]) # 2. Furniture
            time.sleep(self.cd["list_timing"])
            print(lore["shop8"]) # 3. Fishing rods
            time.sleep(self.cd["list_timing"])
            print(lore["shop9"]) # 4. Lures [TODO]
            time.sleep(self.cd["list_timing"])
            print(lore["shop10"]) # 5. Miscellaneous
            time.sleep(self.cd["list_timing"])
            print(lore["shop11"]) # 0. Return
            time.sleep(self.cd["text_timing"])
    
            try:
                isle = int(input("\n> "))
            except ValueError:
                clear()
                print(lore["shop12"]) # You walk into a wall
                time.sleep(self.cd["text_timing"])
            
            if isle == 0:
                clear()
                print(lore["shop14"]) # You exit the store, Your pockets feeling emptier...or heavier, in the medium you can't tell.
                time.sleep(self.cd["read_timer"])
                clear()
                return
        
            match isle:
                case 1:
                    time.sleep(self.cd["text_timing"])
                    clear()
                    self.shop("house", data, sales, lore)
                case 2:
                    time.sleep(self.cd["text_timing"])
                    clear()
                    self.shop("furniture", data, sales, lore)
                case 3:
                    time.sleep(self.cd["text_timing"])
                    clear()
                    self.shop("lake", data, sales, lore)
                case 4:
                    time.sleep(self.cd["text_timing"])
                    clear()
                    print("TODO")
                    continue
                case 5:
                    time.sleep(self.cd["text_timing"])
                    clear()
                    self.shop("misc", data, sales, lore)
                case _:
                    time.sleep(self.cd["text_timing"])
                    clear()
                    print(lore["shop13"]) # Another wall. whats with all these walls?
                    time.sleep(self.cd["text_timing"])
                    continue