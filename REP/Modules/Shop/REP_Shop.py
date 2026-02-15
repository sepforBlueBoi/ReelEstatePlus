#SHOP
import os
import time
import random

def clear():
    os.system('cls' if os.name == "nt" else "clear")
    
def item_display(item, desc):
    print("stall")
    
def shop(tag, data, sale, lore):
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
        time.sleep(1.4)
        print("\n")
        
        for k, v in data["shop"].items(): #grabs item, and item info for each item in shop dict
            if v.get("tag") == tag: # checks if they are in the tag selected
                item_display = k.replace("_", " ")
                if k not in items:
                    items.append(k) # appends item to items list for later selection
                desc = v
                print(f"{desc.get("id")}. - {item_display}") # print items
                time.sleep(0.2)
        print(lore["shop11"]) # 0. Return
                
        try:
            item = int(input("> "))
        except ValueError:
            print() # You hear a loud buzzer blare
    
def shop_init(data, lore):
    print(lore["shop1"]) # you walk into the little shop. the bell above the door dings
    time.sleep(1.4)
    print(lore["shop2"]) # the Cashier greets you.
    time.sleep(1.4)
    print(lore["shop3"], "\n") # Hello there!
    time.sleep(1.4)
    
    sales = 1.0
    if random.randint(1, 65) == 1:
        sales = 0.5 #sales :)
    
    while True:
        print(lore["shop4"]) # There are a wide array of isles. 
        time.sleep(1.4)
        print(lore["shop5"], "\n") # including an isle for houses. sadly It's just the map and keys to the houses.
        time.sleep(1.4)
       
        print(lore["shop6"]) # 1. Real Estate
        time.sleep(0.2)
        print(lore["shop7"]) # 2. Furniture
        time.sleep(0.2)
        print(lore["shop8"]) # 3. Fishing rods
        time.sleep(0.2)
        print(lore["shop9"]) # 4. Lures [TODO]
        time.sleep(0.2)
        print(lore["shop10"]) # 5. Miscellaneous
        time.sleep(0.2)
        print(lore["shop11"]) # 0. Return
        time.sleep(1.4)
    
        try:
            isle = int(input("\n> "))
        except ValueError:
            clear()
            print(lore["shop12"]) # You walk into a wall
            time.sleep(1.4)
            
        if isle == 0:
            clear()
            print(lore["shop14"]) # You exit the store, Your pockets feeling emptier...or heavier, in the medium you can't tell.
            time.sleep(4.5)
            clear()
            return
        
        match isle:
            case 1:
                time.sleep(1.4)
                clear()
                shop("house", data, sales, lore)
            case 2:
                time.sleep(1.4)
                clear()
                shop("furniture", data, sales, lore)
            case 3:
                time.sleep(1.4)
                clear()
                shop("lake", data, sales, lore)
            case 4:
                time.sleep(1.4)
                clear()
                print("TODO")
                continue
            case 5:
                time.sleep(1.4)
                clear()
                shop("misc", data, sales, lore)
            case _:
                time.sleep(1.4)
                clear()
                print(lore["shop13"]) # Another wall. whats with all these walls?
                time.sleep(1.4)
                continue