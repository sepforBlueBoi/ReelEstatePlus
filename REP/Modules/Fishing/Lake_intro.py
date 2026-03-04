import os, sys
import time
import random

def clear():
    os.system('cls' if os.name == "nt" else "clear")
    
fish: dict[str, dict[str, list[str]]]= { # nested dict. you can see how it works RIGHT below.
    "common": {
        "basic ahh fish": ["You caught the basic ahh fish", "You regret fishing. basic ahh fish.", "Basic ahh fish. lame."],
        "other basic ahh fish": ["Other basic ahh fish...", "even lamer then the first basic fish.", "Could have been a better fish. instead you got the other basic fish."],
        "grey fish": ["grey fish caught", "dull. grey fish.", "grey fish caught sadly."],
        "not cool fish": ["You caught the 'not cool fish'", "its a not cool fish. not cool.", "not cool fish. makes you wonder where to cool fish is?"],
        "possibly your pet fish": ["you caught a familiar fish. It's possibly your pet fish", "possibly your pet fish...cool.", "fred, your pet gold fish was found!"]
    },
    "uncommon": {
        "not as bad fish": ["you caught a 'not as bad fish'. not bad.", "this fish isnt as bad. its a not as bad fish.", "not as bad fish caught."],
        "catfish": ["You have found a catfish!", "Catfish caught!", "for once a actual fish! a catfish!"],
        "dogfish": ["You have found a...dogfish?", "At the end of your line something barks. a dogfish.", "as opposed to the catfish, this type of dogfish is not real."],
        "lightgrey fish": ["this fish is a better grey fish. lightgrey fish", "you have obtained a lightgrey fish!", "its almost silver. its a fish. its a lightgrey fish"],
        "bronze fish": ["A bronze fish. it was probably idolized in 1200 BCE", "you have caught a cool bronze fish!", "you have caught a (almost) copper fish."]
    },
    "rare": {
        "Silver fish": ["A silver fish...isnt this a bug?", "You have caught a silver fish. where is the gold fish?", "Silver fish obtained, good thing this isnt minecraft ;)"],
        "lightest grey fish": ["the lightest grey fish caught. its basically white", "You have surfaced the Lightest grey fish", "The lightest grey fish. despite the use of 'the', there are many."],
        "coolest fish": ["This is one of the 'coolest fish'. ", "coolest fish found", "Its not actually a one of a kind, but its a coolest fish."],
        "almost rainbow fish": ["You have caught the 'Almost rainbow fish'", "An almost rainbow fish. missing the blue. i wonder where it went?", "an almost rainbow fish, still with all its scales"],
        "lake squid": ["You caught a lake squid", "weridly enough, you caught a...lake squid", "You have found the never before seen lake squid"],
    }
}

common_payout_range: int = random.randint(50, 100)
uncommon_payout_range: int = random.randint(100, 200)
rare_payout_range: int = random.randint(250, 350)

def lake_init(data, lore, cd): # lake intro wooo. fun.
    """fish intro for reel estate plus."""
    print()# You Walk the path to the lake.
    print() # some birds fly over head.
    
    print() # 1. fish
    print() # 2. return
    
    try:
        choice:int = int(input("> "))
    except ValueError:
        print() # You still cant climb a tree.
        
    if choice == 1:
        #fisher():
        print() 
    elif choice == 2:
        return
    else:
        print() # you slip in the mud and roll up a hill.