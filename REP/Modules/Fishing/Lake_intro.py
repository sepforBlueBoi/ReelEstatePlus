import os, sys
import time

def clear():
    os.system('cls' if os.name == "nt" else "clear")
    
fish: dict[str, dict[str, list[str]]]= {
    "common": {
        "basic ahh fish": ["You caught the basic ahh fish", "You regret fishing. basic ahh fish.", "Basic ahh fish. lame."],
        "other basic ahh fish": ["Other basic ahh fish...", "even lamer then the first basic fish.", "Could have been a better fish. instead you got the other basic fish."],
        "grey fish": ["grey fish caught", "dull. grey fish.", "grey fish caught sadly."],
        "not cool fish": ["You caught the 'not cool fish'", "its a not cool fish. not cool.", "not cool fish. makes you wonder where to cool fish is?"],
        "possibly your pet fish": ["you caught a familiar fish. It's possibly your pet fish", "possibly your pet fish...cool.", "fred, your pet gold fish was found!"]
    },
    "uncommon": {
        "not as bad fish": ["", "", ""],
        "cat fish": ["", "", ""],
        "dog fish": ["", "", ""],
        "lightgrey fish": ["", "", ""],
        "bronze fish": ["", "", ""]
    },
    "rare": {
        "Silver fish": ["", "", ""],
        "lightest grey fish": ["", "", ""],
        "coolest fish": ["", "", ""],
        "almost rainbow fish": ["", "", ""],
        "lake squid": ["You caught a lake squid", "weridly enough, you caught a...lake squid", "You have found the never before seen lake squid"],
    }
}

def lake_init(data, lore, cd): # lake intro wooo. fun.
    """fish intro for reel estate plus."""
    print()# You Walk the path to the lake.