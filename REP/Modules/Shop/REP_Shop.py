#SHOP
import os
import time

def clear():
    os.system('cls' if os.name == "nt" else "clear")
    
def shop(tag, data, sale):
    print("stall")
    
def shop_init(data, lore):
    print() # you walk into the little shop. the bell above the door dings
    print() # the Cashier greets you.
    print() # Hello there!
    
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