# -*- coding: utf-8 -*-

import random
import os
import time

def clear():
    os.system('cls' if os.name == "nt" else "clear")

def slot_animation():
    reel = []
    for i in range(3):
        item = random.choice(["\U0001f48e","\u2764\ufe0f", "\U0001F34B", "\U0001F514", "\U0001F340", "7"]) #diamond, heart, lemon, bell, clover
        reel.append(item)

    for times in [0.1 ,0.15, 0.2, .27, 0.4]:    
        for i in range(5):
            clear()
            chance = random.choice(["\U0001f48e","\u2764\ufe0f", "\U0001F34B", "\U0001F514", "\U0001F340", "7"])
            print(f"| {chance} |")
            time.sleep(times)

    for times in [0.1 ,0.15, 0.2, .27, 0.4]:    
        for i in range(5):
            clear()
            chance = random.choice(["\U0001f48e","\u2764\ufe0f", "\U0001F34B", "\U0001F514", "\U0001F340", "7"])
            print(f"| {reel[0]} | {chance} |")
            time.sleep(times)

    for times in [0.1 ,0.15, 0.2, 0.27, 0.4]:    
        for i in range(5):
            clear()
            chance = random.choice(["\U0001f48e","\u2764\ufe0f", "\U0001F34B", "\U0001F514", "\U0001F340", "7"])
            print(f"| {reel[0]} | {reel[1]} | {chance} |")
            time.sleep(times)

    print(f"   _    _    _")
    print(f" | {reel[0]} | {reel[1]} | {reel[2]} | ,")
    print(" |              |/")


    return reel

