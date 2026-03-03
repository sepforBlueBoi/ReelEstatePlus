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
    
    Contains multiple pages, at then end of each page will be a prompt.
    type in the page you wanna go to. or do i use a and d to move between pages? hmmm
     a and d would just require adding of subtracting one, and would mirror every other games inventory.
     i will do the number method as it is not used, and i want to juice the freedom i have as a text based game
     ^-Not Important
     
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
        for h in data["estate"].items():
            if h:
                house = h.replace("_", " ")
                print(f"\t{house}")
                houses = True
        if not houses:
            print("\tYou are Homeless...once again.")
                
        print("\nActive furniture: ")
        for i in data["furniture"].items():
            if i:
                furniture = i.replace("_", " ")
                if fur_phase[i] == data["phase"]:
                    print(f"{furniture}")
            furnitur = True
        if not furnitur:
            print("\tYou have not any furniture")
        
    def page_4(self, data):
        print("page 4\t ----\tFishpedia\n")
        time.sleep(self.cd["text_timing"])    
        
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
        print(f"[{data["name"]}]") # user name
        time.sleep(self.cd["list_timing"])
        print(data["c_name"],":",data["currency"]) # currency
        time.sleep(self.cd["list_timing"])
        print("tokens:", data["tokens"]) # tokens
        time.sleep(self.cd["list_timing"])
        if data["map"]:
            print("Map")
            
        for i in data["misc"]:
            if i == True:
                item = i.replace("_", " ")
                print(item)
        
        print("\nFishing rods: ") # fishing rods
        for i in data["lake"].items():
            if i:
                thing = i.replace("_", " ")
                time.sleep(self.cd["list_timing"])
                print(f"\t{thing}")
                rods = True
        if not rods:
            print("No rods owned.")
                
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
            page_string = str(self.page) #<- making it a string so maybe it works better???. this is where the error is
            page_to_display = getattr(self, f"page_{page_string}") # <- getattr. even when not making self.page a string an error occurs here too
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
        
        
# for quick testing skeleton. 
# does not work with data parameter
# probably wont touch this again, but i'd like to be safe ;)        
"""Inv = Inventory() # instance of the call.
Inv.display() # <- the call"""