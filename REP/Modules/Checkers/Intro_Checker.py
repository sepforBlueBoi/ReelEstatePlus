bad_names = ["poopfart", "poop fart", "fart poop", "fartpoop", "poopfarts", "poop farts", "fartpoops", "fart poops"]
wd_names = ["gaster", "wdgaster", "wd gaster", "wd", "w d", "w d gaster"]

def name_checker(name):
    """list of if statements to see if name is good. """
    lname = name.lower().strip()
    if lname == "":
        return "try again"
    elif lname in bad_names:
        return "try again" 
    elif lname == "job":
        return "try again"
    elif lname in wd_names:
        return "banished"
    else:
        return "good"
    
def money_n_checker(Mname):
    """list of if statementes to see if currency name is good"""
    lmname = Mname.lower().strip()
    if lmname == "":
        return "try again"
    elif lmname in bad_names:
        return "try again"
    elif lmname == "job":
        return "try again"
    else:
        return "good"
    
def epic_name_checker(name):
    """long list of if statements to see if your name can trigger an easter egg!"""
    lname = name.lower().strip()
    if lname == "kondike":
        return "Hello Dev ;)"
    elif lname == "no2no":
        return "not goku?"
    elif lname == "minecraft man" or lname == "aredstoneengineer":
        return "didnt know you'd show up. nice"
    elif lname in ["fryinnpan", "pan", "fry", "white monster"]:
        return "welcome back streamer :D"
    elif lname == "goku":
        return "hello no2 :)"
    elif lname == ["rauan", "rauanb"]:
        return "you're playing?? crazy"
    else:
        return "Welcome!"