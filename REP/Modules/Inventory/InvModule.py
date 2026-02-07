# so borad. inventory...build your self please
#...
# FINE, I'll do it :\
import time
import os

def clear():
    os.system('cls' if os.name == "nt" else "clear")
    
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
        self.data = {} # Holds data. same thing we did in Hub.py
        self.page = 1 # keep track of pages
        
    def page_5(self, data):
        print("page 5\t ----\tHouses and Furniture")
        time.sleep(1.4)
        
    def page_4(self, data):
        print("page 4\t ----\tFishpedia")
        time.sleep(1.4)    
        
    def page_3(self, data):
        print("Page 3\t ----\tAchievments")
        time.sleep(1.4)    
        
    def page_2(self, data):
        print("Page 2\t ----\tCollectables")
        time.sleep(1.4)
        
    def page_1(self, data): # <- current page function
        print("Page 1\t ----\tBasic Inventory")
        time.sleep(1.4)
        print(data["name"])
        time.sleep(0.9)
        print(data["c_name"], ":", data["currency"])
        time.sleep(0.9)
        print("tokens:", data["tokens"])
        time.sleep(0.9)
        print("Fishing rods: TODO") #TODO 
        time.sleep(0.9)
        
    def prompt(self): # simple page prompt that will be at the bottom of every page.
        time.sleep(1.4)
        print(f"page {self.page}/5")
        time.sleep(1.4)
        print("which page . . .")
        time.sleep(1.4)
        print("0 to close inventory")
        time.sleep(1.4)
        try:
            page = int(input("> ").strip())
        except ValueError:
            return "error"
        
        return page

    def display(self, data):
        while True:
            clear()
            page_string = str(self.page) #<- making it a string so maybe it works better???. this is where the error is
            page_to_display = getattr(self, f"page_{page_string}") # <- getattr. even when not making self.page a string an error occurs here too
            page_to_display(data)
        
            page = self.prompt()
            
            if page == "error":
                print("You proceed to change the channel. you are still on the same page") 
                continue
            
            if page == 0:
                print("you close the inventory")
                return
            
            self.page = page
            continue
        
        
# for quick testing skeleton. 
# does not work with data parameter
# probably wont touch this again, but i'd like to be safe ;)        
"""Inv = Inventory() # instance of the call.
Inv.display() # <- the call"""