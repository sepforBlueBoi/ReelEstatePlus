# so bored. inventory...build your self please
#...
# FINE, I'll do it :\
import time
import sys, gc
import random

def clear() -> None:
    sys.stdout.write("\033[H\033[2J\033[3J")
    
fur_phase: dict[str, int] = {
        "Old_Couch": 1,
        "Small_TV": 1,
        "Smelly_Rug": 1,
        "Nice_Loveseat": 2,
        "Basic_TV": 2,
        "Nice_Rug": 2,
        "Pictures": 2,
        "Desk": 2,
        "Deluxe_Double_decker_couch": 3,
        "Amazing_Carpet": 3,
        "more_pictures": 3,
        "Gaming_chair": 3,
        "Entire_Desktop": 3,
        "Statue_of_self": 3
    }
    
class InvDisplay:
    """Inventory class for reel estate plus.
     
     Each page will be different but will still be on the same function. 
     Each page gets its own function: basic, fishpedia, etc.
     but its all displayed in ONE function.
     ^-Important
     """
    __slots__ = ["page", "cd"]
     
    def __init__(self):
        self.page: int = 1 # keep track of pages
        self.cd: dict = {}

    def equip_func(self, data: dict, ToEquip: str) -> None:
        header: str = ""
        ItemsToCycleThrough: list[str] = []
        ItemsToSelect: list[str] = []

        if ToEquip == "rod":
            header: str = "Rod Equip Menu"
            rods_list: list[str] = ["lake", "ocean"]
            ItemsToCycleThrough.extend(rods_list)
        elif ToEquip == "lures":
            header:str = "Lure Equip Menu"
            ItemsToCycleThrough.append("lures")

        clear()

        while True:
            print(f"[{header}]\n")
            time.sleep(self.cd["text_timing"])
        
            idx: int = 1
            for item in ItemsToCycleThrough:
                for itemSquared, boolean in data[item].items():
                    if boolean:
                        itemSquared_display: str = itemSquared.replace('_', ' ')
                        if itemSquared == data["equipped_rod" if ToEquip == "rod" else "equipped_lure"]:
                            print(f"{idx} - {itemSquared_display}**")
                        else:
                            print(f"{idx} - {itemSquared_display}")
                        if not itemSquared in ItemsToSelect:
                            ItemsToSelect.append(itemSquared)
                        time.sleep(self.cd["list_timing"])
                        idx += 1

            print("0 - Return to main page")
           
            equip_select: int = 101509
            try:
                equip_select: int = int(input("> "))
            except ValueError:
                print("misinput?")
                time.sleep(self.cd["read_timer"])
                clear()
                continue


            if equip_select == 0:
                clear()
                return

            if equip_select > len(ItemsToSelect):
                clear()
                print("We both know thats out out of range") #FIXME Proper humor fail message please
                continue
            
            item: str = ItemsToSelect[equip_select - 1]

            if item == data["equipped_rod" if ToEquip == "rod" else "equipped_lure"]:
                clear()
                print("You cannot equip something twice.")
                continue
            
            if ToEquip == "rod":
                data["equipped_rod"] = item
            else:
                data["equipped_lure"] = item

            time.sleep(self.cd["text_timing"])
            print(f"Item {item} equipped")
            time.sleep(self.cd["read_timer"])
            clear()

            ItemsToSelect.clear() # Make sure this list doesnt keep filling :)
            continue

        

    def page_6(self, data: dict) -> None:
        while True:
            clear()
            print("Page 6\t ----\tEquip Station\n")
            time.sleep(self.cd["text_timing"])
            print('\n')

            print("1. Equip Rod")
            time.sleep(self.cd["list_timing"])
            print("2. Equip Lure")
            time.sleep(self.cd["list_timing"])
            print("0. Page Prompt")
            time.sleep(self.cd["text_timing"])
            
            equip_choice: int = 83

            try:
                equip_choice: int = int(input("> "))
            except ValueError:
                pass

            match equip_choice:
                case 1:
                    self.equip_func(data, "rod")
                case 2:
                    self.equip_func(data, "lures")
                case 0:
                    break
                case _:
                    clear()
                    print("You cannot equip furniture, please try again.")
                    time.sleep(self.cd["read_timer"])
                    clear()
                    continue

    def page_5(self, data: dict) -> None:
        houses = False
        furnitur = False
        print("page 5\t ----\tHouses and Furniture\n")
        time.sleep(self.cd["text_timing"])
        print("houses owned: ")
        for k, v in data["estate"].items():
            if v:
                house = k.replace("_", " ")
                print(f"\t{house}")
                houses = True
        if not houses:
            print("\tYou are Homeless...once again.")
                
        print("\nActive furniture: ")
        for k, v in data["furniture"].items():
            if v:
                furniture = k.replace("_", " ")
                if fur_phase[k] == data["phase"]:
                    print(f"{furniture}")
                furnitur = True
        if not furnitur:
            print("\tYou have not any furniture")
        
    def page_4(self, data):
        print("page 4\t ----\tFishpedia\n")
        time.sleep(self.cd["text_timing"])  
        idx = 1
        for rarity, fishes in data["fish"].items():
            for fish_name, caught in fishes.items():
                if caught:
                    print(f"{idx}. {fish_name} [{rarity}]")
                else:
                    print(f"{idx}. ??? [???]")
                time.sleep(self.cd["list_timing"])
                idx += 1
            
    def page_3(self, data: dict) -> None:
        print("Page 3\t ----\tAchievements\n")
        time.sleep(self.cd["text_timing"])    
        
    def page_2(self, data: dict) -> None:
        print("Page 2\t ----\tCollectables and Lore\n")
        time.sleep(self.cd["text_timing"])
        
    def page_1(self, data: dict) -> None: # <- current page function
        rods = False
        print("Page 1\t ----\tBasic Inventory\n")
        time.sleep(self.cd["text_timing"])
        print(f"[{data['name']}]") # user name
        time.sleep(self.cd["list_timing"])
        print(data["c_name"],":",data["currency"]) # currency
        time.sleep(self.cd["list_timing"])
        print("tokens:", data["tokens"]) # tokens
        time.sleep(self.cd["list_timing"])
        if data["Map"]:
            print("Map")
            
        for k, v in data["misc"].items():
            if v == True:
                item = k.replace("_", " ")
                print(item)
        
        print("\nFishing rods: ") # fishing rods
        for k, v in data["lake"].items():
            if v:
                thing = k.replace("_", " ")
                time.sleep(self.cd["list_timing"])
                print(f"\t{thing}")
                rods = True
        if not rods:
            print("\tNo rods owned.")
                
        time.sleep(self.cd["list_timing"])
        
    def prompt(self) -> int: # simple page prompt that will be at the bottom of every page.
        time.sleep(self.cd["list_timing"])
        print(f"page {self.page}/6")
        time.sleep(self.cd["list_timing"])
        print("which page . . .")
        time.sleep(self.cd["list_timing"])
        print("0 to close inventory")
        print("1-6 to go to those pages")
        time.sleep(self.cd["list_timing"])
        try:
            page: int = int(input("> ").strip())
        except ValueError:
            return 404
        
        
        if page in [0, 1, 2, 3, 4, 5, 6]:
            return page
        else:
            return 404

    def display(self, data: dict, cd: dict) -> None:
        self.cd = cd
        sys.stdout.write(f'\033]0;Inventory\a')
        sys.stdout.flush()
        while True:
            clear()
            page_to_display = getattr(self, f"page_{self.page}") 
            page_to_display(data)

            print("\n")
            
            page = self.prompt()
            
            if page == 404:
                print("You proceed to change the channel. you are still on the same page") 
                continue
            
            if page == 0:
                clear()
                print("you close the inventory")
                time.sleep(self.cd["read_timer"])
                clear()
                gc.collect()
                return

            if random.randint(1, 6) == 2:
                gc.collect()
            
            self.page = page
            continue
        
