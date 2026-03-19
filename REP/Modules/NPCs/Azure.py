import os, gc, time
from REP.Modules.Save_Modules.Load_module import load_json
from colorama import Fore, Style

Azure: dict[str, dict[str, str]] = load_json("MyDialogue.json")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro_talk(cd: dict[str, float], save: dict[str, Any]):
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
    time.sleep(timer)
    print(Fore.LIGHTBLUE_EX + Azure["Azure"]["Azu_enc1_text_8"] + Style.RESET_ALL)
    time.sleep(timer)
    print(Azure["narrator"]["nar_enc1_text_6"])
    time.sleep(timer)
    print(Fore.LIGHTBLUE_EX + Azure["Azure"]["Azu_enc1_text_9"] + Style.RESET_ALL)
    time.sleep(timer)
    print(Azure["narrator"]["nar_enc1_text_7"].replace("*", save["name"]))
    time.sleep(timer)

    print(Azure["player"]["ply_enc1_text_1"])
    time.sleep(cd["list_timing"])
    print(Azure["player"]["ply_enc1_text_2"])
    time.sleep(cd["list_timing"])

    not_important: str = input("> ").strip()
    time.sleep(timer)
    
    if not_important in ["1", "2"]:
        # Normal
        print(Azure["narrator"]["nar_enc1_text_8-1"])
    else:
        # Gibberish
        print(Azure["narrator"]["nar_enc1_text_8-2"])

        
 
