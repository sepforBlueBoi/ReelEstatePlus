import copy
game_dict: dict[str, any] = {
    "name": "",
    "currency": 250,
    "tokens": 0,
    "c_name": "",
    "map": False,
    "intro": False,    
    "ocean_unlock": False,
    "has_met_azure": False,
    "phase": 1,
    "fish_caught": 0,
    "equipped_rod": None,
    "equipped_lure": None,
    
    "achiev": {
      
    },
    "quests": {
        
    },
    "collectables": {
        
    },
    "lore": {
        
    },
    "lake": {
        "Old_Rod": False,
        "Basic_Rod": False
    },
    
    "ocean": {
        "Colored_Rod": False,
        "Efficient_Rod": False,
        "Superior_Rod": False,
        "Premier_Rod": False
    },
    
    "fish": {
        "common": {
            "basic ahh fish": False,
            "other basic ahh fish": False,
            "grey fish": False,
            "not cool fish": False,
            "possibly your pet fish": False
        },
        "uncommon": {
            "not as bad fish": False,
            "catfish": False,
            "dogfish": False,
            "lightgrey fish": False,
            "bronze fish": False
        },
        "rare": {
            "Silver fish": False,
            "lightest grey fish": False,
            "coolest fish": False,
            "almost rainbow fish": False,
            "lake squid": False 
            },
    },
    "lures": {
            "Basic_lure": False,
            "Scented_lure": False,
            "Superior_lure": False,
            "Magic_Worm": False
    },
    "estate": {
         "Small_House": False,
        "House": False,
        "Large_House": False,
        "Weird_House": False,
        "Box": False,
        "Casino": {"owned": False, "lock": True}
    },
    "furniture": {
        "Old_Couch": False,
        "Small_TV": False,
        "Smelly_Rug": False,
        "Nice_Loveseat": False,
        "Basic_TV": False,
        "Nice_Rug": False,
        "Pictures": False,
        "Desk": False,
        "Deluxe_Double_decker_couch": False,
        "Amazing_Carpet": False,
        "more_pictures": False,
        "Gaming_chair": False,
        "Entire_Desktop": False,
        "Statue_of_self": False
    },
    
    "misc": {
        "Red_and_White_Ball": False,
        "Golden_Idle": False,
    },
}

def new_game():
    return copy.deepcopy(game_dict)
