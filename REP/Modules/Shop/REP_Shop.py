#SHOP
import os
import time
import random

def clear():
    os.system('cls' if os.name == "nt" else "clear")
    
    
shop: dict[str, any] = { #replica of all items but with prices.
        "Small_House": {"tag": "estate", "price": 2000, "desc": "Basic house, perfect for one person.", "id": 1},
        "House": {"tag": "estate", "price": 2500,"desc": "Rather nice house, perfect for you.", "id": 2},
        "Large_House": {"tag": "estate", "price":5000, "desc": "Large house. Not mansion sized yet.", "id": 3},
        "Weird_House": {"tag": "estate", "price": 6300, "desc": "This house has 20 bathrooms. 19 of them have toilets. 1 has a urinal.", "id": 4},
        "Box": {"tag": "estate", "price": 2, "desc": "how...is this a house?", "id": 5},
        "Casino": {"tag": "estate", "price": 9500, "desc": "Not a house. but you can live in it. Something inside wants you.", "lock": True, "id": 6},
        "Old_Rod": {"tag": "lake", "price": 5, "desc": "Old fishing rod. kinda broken. I would not advice using it.", "id": 1},
        "Basic_Rod": {"tag": "lake", "price": 450, "desc": "Basic rod. decent choice for the lake.", "id": 2},
        "Colored_Rod": {"tag": "ocean", "price": 600, "desc": "comes in many different colors", "colors": ["red", "orange", "yellow", "green", "blue", "indigo", "pruple"],
                        "color_owned": "", "id": 1},
        "Effiecent_Rod": {"tag": "ocean", "price": 800, "desc": "Great rod. good for fishing at the beach", "id": 2},
        "Superior_Rod": {"tag": "ocean", "price": 1200, "desc": "One of the best rods to wield. I bet you will be catching great fish at the beach", "id": 3},
        "Premier_Rod": {"tag": "ocean", "price": 2000, "desc": "The best rod. His name is Rodney.", "id": 4},
        "Map": {"tag": "misc", "price": 500, "desc": "Its the same map you refused at the beginning of the game.", "id": 1},
        "Red_and_White_Ball": {"tag": "misc", "price": 450, "desc": "It's a weird red and white capsule. possibly to contain some weird pocket monster?", "id": 2},
        "Golden_Idle": {"tag": "misc", "price": 9, "desc": "It's a golden idle. You aren't sure if you should waste your money on this.", "id": 3},
        "Old_Couch": {"tag": "furniture", "phase": 1, "price": 50, "desc": "it is mostly holes", "id": 1},
        "Small_TV": {"tag": "furniture", "phase": 1, "price": 100, "desc": "Its basically a mobile phone with how small it is.", "id": 2},
        "Smelly_Rug": {"tag": "furniture", "phase": 1, "price": 25, "desc": "It has one stain, It wont leave. Its smell is...Why was this for sell?", "id": 3},
        "Nice_Loveseat": {"tag": "furniture", "phase": 2, "price": 200, "desc": "Thousands of times better then the couch. No holes either.", "id": 1},
        "Basic_TV": {"tag": "furniture", "phase": 2, "price": 600, "desc": "It comes with all modern streaming services for free!. this has gotta be illegal", "id": 2},
        "Nice_Rug": {"tag": "furniture", "phase": 2, "price": 350, "desc": "Its the same type of rug from before; just clean and new.", "id": 3},
        "Pictures": {"tag": "furniture", "phase": 2, "price": 100, "desc": "There is three of them. sadly since this world text based you can't see their beauty.", "id": 4},
        "Desk": {"tag": "furniture", "phase": 2, "price": 200, "desc": "Presumably for a computer you don't have yet.", "id": 5},
        "Deluxe_Double_decker_couch": {"tag": "furniture", "phase": 3, "price": 1000, "desc": "surprisingly not made of Legos.", "id": 1},
        "Amazing_Carpet": {"tag": "furniture", "phase": 3, "price": 550, "desc": "Its actually a carpet of snow that doesn't melt, nor get footprints. It's almost solid.", "id": 2},
        "more_pictures": {"tag": "furniture", "phase": 3, "price": 100, "desc": "Even more pictures you can't see. just know, they are beautiful.", "id": 3},
        "Gaming_chair": {"tag": "furniture", "phase": 3, "price": 150, "desc": "Would fit well with the desk you bought earlier.", "id": 4},
        "Entire_Desktop": {"tag": "furniture", "phase": 3, "price": 1600, "desc": "Even comes with a monitor, keyboard, and mouse. weird.", "id": 5},
        "Statue_of_self": {"tag": "furniture", "phase": 3, "price": 9000, "desc": "...who made this and when?", "id": 6}
    }
    
class Shop:

    def __init__(self):
        self.cd = {}
    
    def item_display_function(self, item, price): # item display logic for polish. 
    
        shop_item = item.replace("_", " ")
        print(f"====={shop_item}=====")
        print("\n")
        time.sleep(self.cd["text_timing"])
    
        print(shop[item].get("desc"))
        time.sleep(self.cd["text_timing"])
    
        if price != shop[item].get("price"):
            Price = f"[{shop[item].get("price")}] -> {price}"
        
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
            case "estate":
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
        
            for k, v in shop.items(): #grabs item, and item info for each item in shop dict
                if v.get("tag") == tag: # checks if they are in the tag selected
                    if not v.get("phase") or v.get("phase") == data["phase"]: # makes sure you in the correct phase if its there (ie furniture.) so it doesnt add ALL furniture to the list.
                        item_display = k.replace("_", " ")
                        if k not in items:
                            items.append(k) # appends item to items list for later selection
                        print(f"{shop[k].get("id")}. - {item_display}") # print items
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
                price = round(shop[items[item]].get("price") * sale)
                clear()
                self.item_display_function(items[item], price) # Display item, item descripton, and price, for UI
            
                print()# 1. Buy/OWNED
                print()# 2. Cancel
            
                try:
                    choice = input("> ")
                except ValueError:
                    print() # Im Concerned.

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
                    self.shop("estate", data, sales, lore)
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