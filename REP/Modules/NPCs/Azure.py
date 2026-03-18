import os, gc, time
from REP.Modules.Save_Modules.Load_module import load_json
from colorama import Fore, Style

Azure = load_json("MyDialogue.json")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro_talk(cd: dict):
    timer: float = cd["text_timing"]
    print(Azure["narrator"]["nar_enc1_text_1"])
    time.sleep(timer)
    print(Azure["narrator"]["nar_enc1_text_2"])
    time.sleep(timer - 0.5)
    print(Fore.LIGHTBLUE_EX + Azure["Azure"]["Azu_enc1_text_1"])
    time.sleep(timer)
    print(Fore.LIGHTBLUE_EX + Azure["Azure"]["Azu_enc1_text_2"] + Style.RESET_ALL)
    time.sleep(timer - 0.5)
    print(Azure["narrator"]["nar_enc1_text_3"])
    time.sleep(timer)
    print(Fore.LIGHTBLUE_EX + Azure["Azure"]["Azu_enc1_text_3"] + Style.RESET_ALL)
    time.sleep(timer + timer)
    print(Azure["narrator"]["nar_enc1_text_4"])
    time.sleep(timer)
    print(Fore.LIGHTBLUE_EX + Azure["Azure"]["Azu_enc1_text_4"])
    time.sleep(timer)
    print(Azure["Azure"]["Azu_enc1_text_5"])
    time.sleep(timer)
    print(Azure["Azure"]["Azu_enc1_text_6"])
    time.sleep(timer)
    print(Azure["Azure"]["Azu_enc1_text_7"].replace("They", Fore.RED + "They") + Style.RESET_ALL)
    time.sleep(timer - 0.5)
    print(Azure["narrator"]["nar_enc1_text_5"].replace("Player", Fore.RED + "Player") + Style.RESET_ALL)
    
    # reference from the json file
    """"Azure": {
        "Azu_enc1_text_1": "Shut up.",
        "Azu_enc1_text_2": "I Have a name. You obnoxious piece of shi-",
        "Azu_enc1_text_3": "Why isn't yours?",
        "Azu_enc1_text_4": "Of course you wouldn't know.",
        "Azu_enc1_text_5": "You are a humble narrator,",
        "Azu_enc1_text_6": "And I'm an outsider.",
        "Azu_enc1_text_7": "But if They have been here before-"
    },

    "narrator": {
        "nar_enc1_text_1": "You walk into 'Azure's cove'.",
        "nar_enc1_text_2": "The nameless shop keeper greets yo-",
        "nar_enc1_text_3": "What...Why is your text...blue?",
        "nar_enc1_text_4": "Im sorry? I dont remember you ever in the memo i was given.",
        "nar_enc1_text_5": "No. You cannot reference the Player like that."
    }"""