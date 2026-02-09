#SHOP
import os
import time
import random

def clear():
    os.system('cls' if os.name == "nt" else "clear")
    
def shop(tag, data, sale):
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
    """
    match tag:
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
        print("\n")
        
        for idx, (k, v) in enumerate(data["shop"].items(), start=1):
            if v.get("tag") == tag:
                item = k.replace("_", " ")
                print(f"{idx}. - {item}")
                
        input()
        
    
def shop_init(data, lore):
    print() # you walk into the little shop. the bell above the door dings
    print() # the Cashier greets you.
    print() # Hello there!
    
    sales = 1.0
    if random.randint(1, 40) == 1:
        sales = 0.5
    
    while True:
        print() # There are a wide array of isles. 
        print() # including an isle for houses. sadly It's just the map and keys to the houses.
       
        print() # 1. Real Estate
        print() # 2. Furniture
        print() # 3. Fishing rods
        print() # 4. Lures [TODO]
        print() # 5. Miscellaneous
        print() # 0. Return
    
        try:
            isle = int(input())
        except ValueError:
            print() # You walk into a wall
            
        match isle:
            case 1:
                shop("house", data, sales)
            case 2:
                shop("furniture", data, sales)
            case 3:
                shop("lake", data, sales)
            case 4:
                print("TODO")
                continue
            case 5:
                shop("misc", data, sales)
            case 0:
                return
            case _:
                print() # Another wall. whats with all these walls?
                continue