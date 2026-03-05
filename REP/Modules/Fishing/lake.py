import random
import os

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



class Fishing:
    __slots__ = ["player_pos", "column", "ticks", "target", "fish", "column_amount", "payout", "rarity"] # helps with storage.
    
    def __init__(self):
        self.player_pos: int = 0
        self.column: list[str] = []
        self.ticks: list[int] = [5]
        self.target: int = 0
        self.fish: str = ""
        self.column_amount: int = 0
        self.payout: int = 0
        self.rarity: str = ""
        
    def random_gen(self):
        for i in range(8):
            self.column[i] = "\U0001F7E6" # blue sqaures
        
        self.target = random.randint(0, 7)
        self.column[self.target] = "\U0001F7E5" # red sqaures
        
        if self.target > 0: # so we dont get a yellow on NOT beside the red.
            self.column[self.target - 1] = "\u1F7E8" # yellow sqaures
        if self.target < 7: # same as above
            self.column[self.target + 1] = "\u1F7E8"
            
        rarity: list[str] = ["common", "uncommon", "rare"]
        fishes: list[str] = []
            
        self.rarity = random.choices(rarity)
        
        if self.rarity == "common":
            self.column_amount = 2
            self.payout = common_payout_range
        elif self.rarity == "uncommon":
            self.column_amount = 3
            self.payout = uncommon_payout_range
        elif self.rarity == "rare":
            self.column_amount = 4
            self.payout = rare_payout_range    
        
        for k, v in fish[self.rarity].items():
            fishes.append(k)
            
        self.fish = random.choices(fishes)
            
        for i in range(self.column_amount):
            self.ticks.append(4) # stays at four to keep it possible
            
        