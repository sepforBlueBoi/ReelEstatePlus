bad_names = ["poopfart", "poop fart", "fart poop", "fartpoop", "poopfarts", "poop farts", "fartpoops", "fart poops"]
wd_names = ["gaster", "wdgaster", "wd gaster", "wd", "w d", "w d gaster"]

def name_checker(name):
    """list of if statements to see if name is good. """
    lname = name.lower().strip()
    match lname:
        case "":
            return "try again"
        case lname if lname in bad_names:
            return "try again" 
        case "job":
            return "try again"
        case  lname if lname in wd_names:
            return "banished"
        case _:
            return "good"
    
def money_n_checker(Mname):
    """list of if statementes to see if currency name is good"""
    lmname = Mname.lower().strip()
    match lmname:
        case "":
            return "try again"
        case lmname if lmname in bad_names:
            return "try again"
        case "job":
            return "try again"
        case _:
            return "good"
    
def epic_name_checker(name):
    """long list of if statements to see if your name can trigger an easter egg!"""
    lname = name.lower().strip()
    match lname:
        case "kondike":
            return "Hello Dev ;)"
        case "no2no":
            return "not goku?"
        case "minecraft man" | "aredstoneengineer":
            return "didnt know you'd show up. nice"
        case lname if lname in ["fryinnpan", "pan", "fry", "white monster"]:
            return "welcome back streamer :D"
        case "goku":
            return "hello no2 :)"
        case "rauan" | "rauanb":
            return "you're playing?? crazy"
        case _:
            return "Welcome!"