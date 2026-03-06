# so borad. inventory...build your self please
#...
# FINE, I'll do it :\
import time
import os, sys

def clear():
    os.system('cls' if os.name == "nt" else "clear")
    
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
     
    def __init__(self):
        self.data: dict = {} # Holds data. same thing we did in Hub.py
        self.page: int = 1 # keep track of pages
        self.cd: dict = {}
        
    def page_5(self, data):
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
            
    def page_3(self, data):
        print("Page 3\t ----\tAchievements\n")
        time.sleep(self.cd["text_timing"])    
        
    def page_2(self, data):
        print("Page 2\t ----\tCollectables and Lore\n")
        time.sleep(self.cd["text_timing"])
        
    def page_1(self, data): # <- current page function
        rods = False
        print("Page 1\t ----\tBasic Inventory\n")
        time.sleep(self.cd["text_timing"])
        print(f"[{data['name']}]") # user name
        time.sleep(self.cd["list_timing"])
        print(data["c_name"],":",data["currency"]) # currency
        time.sleep(self.cd["list_timing"])
        print("tokens:", data["tokens"]) # tokens
        time.sleep(self.cd["list_timing"])
        if data["map"]:
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
        
    def prompt(self): # simple page prompt that will be at the bottom of every page.
        time.sleep(self.cd["list_timing"])
        print(f"page {self.page}/5")
        time.sleep(self.cd["list_timing"])
        print("which page . . .")
        time.sleep(self.cd["list_timing"])
        print("0 to close inventory")
        print("1-5 to go to those pages")
        time.sleep(self.cd["list_timing"])
        try:
            page: int = int(input("> ").strip())
        except ValueError:
            return "error"
        
        
        if page in [0, 1, 2, 3, 4, 5]:
            return page
        else:
            return "error"

    def display(self, data, cd):
        self.cd = cd
        sys.stdout.write(f'\033]0;Inventory\a')
        sys.stdout.flush()
        while True:
            clear()
            page_string = str(self.page) # this is a string cause of earlier bugs. while it may not NEED to be one, im scared to remove it
            page_to_display = getattr(self, f"page_{page_string}") 
            page_to_display(data)

            print("\n")
            
            page = self.prompt()
            
            if page == "error":
                print("You proceed to change the channel. you are still on the same page") 
                continue
            
            if page == 0:
                clear()
                print("you close the inventory")
                time.sleep(self.cd["read_timer"])
                clear()
                return
            
            self.page = page
            continue
        
