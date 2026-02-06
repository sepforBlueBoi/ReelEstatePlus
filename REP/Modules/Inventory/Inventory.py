# so borad. inventory...build your self please
#...
# FINE, I'll do it :\
import time
import os

def clear():
    os.system('cls' if os.name == "nt" else "clear")
    
class Inventory:
    """Inventory class for reel estate plus.
    
    Contains multiple pages, at then end of each page will be a prompt.
    type in the page you wanna go to. or do i use a and d to move between pages? hmmm
     a and d would just require adding of subtracting one, and would mirror every other games inventory.
     i will do the number method as it is not used, and i want to juice the freedom i have as a text based game
     
     Each page will be different but will still be on the same function. 
     Each page gets its own function: basic, fishpedia, etc.
     but its all displayed in ONE function.
     """
     
    def __init__(self):
        self.data = {}
        self.page = 1 # keep track of pages
        
    def prompt(): # simple page prompt that will be at the bottom of every page.
        time.sleep(1.4)
        print("which page . . .")
        time.sleep(1.4)
        try:
            page = int(input("> ").strip())
        except ValueError:
            return "error"
        
        return page