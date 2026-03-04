def checking(data, lore, cd):
    
    has_rod = False
    
    for k, v in data["lake"].items():
        if v:
            has_rod = True
            
    if has_rod:
        print("plac holder")
        #lake
    else:
        print("placeholder") # You have no rods to fish with. go buy one from spamee'o'jr.
        return