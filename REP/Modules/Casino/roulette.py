import time
import os
import random


def clear():
    os.system('cls' if os.name == "nt" else "clear")


red_win = {
    "frame1": "    🟦\n  🟥  🟥\n🟦      🟦\n  ⬛  🟥\n    🟦\n    ^",
    "frame2": "    🟥\n  🟦  🟦\n🟥      🟥\n  🟦  🟦\n    ⬛\n    ^",
    "frame3": "    🟦\n  🟥  🟥\n🟦      🟦\n  🟥  ⬛\n    🟦\n    ^",
    "frame4": "    🟥\n  🟦  🟦\n🟥      ⬛\n  🟦  🟦\n    🟥\n    ^",
    "frame5": "    🟦\n  🟥  ⬛\n🟦      🟦\n  🟥  🟥\n    🟦\n    ^",
    "frame6": "    ⬛\n  🟦  🟦\n🟥      🟥\n  🟦  🟦\n    🟥\n    ^",
    "frame7": "    🟦\n  ⬛  🟥\n🟦      🟦\n  🟥  🟥\n    🟦\n    ^",
    "frame8": "    🟥\n  🟦  🟦\n⬛      🟥\n  🟦  🟦\n    🟥\n    ^",
}

blue_win = {
    "frame1": "    🟥\n  🟦  🟦\n⬛      🟥\n  🟦  🟦\n    🟥\n    ^",
    "frame2": "    🟦\n  🟥  🟥\n🟦      🟦\n  ⬛  🟥\n    🟦\n    ^",
    "frame3": "    🟥\n  🟦  🟦\n🟥      🟥\n  🟦  🟦\n    ⬛\n    ^",
    "frame4": "    🟦\n  🟥  🟥\n🟦      🟦\n  🟥  ⬛\n    🟦\n    ^",
    "frame5": "    🟥\n  🟦  🟦\n🟥      ⬛\n  🟦  🟦\n    🟥\n    ^",
    "frame6": "    🟦\n  🟥  ⬛\n🟦      🟦\n  🟥  🟥\n    🟦\n    ^",
    "frame7": "    ⬛\n  🟦  🟦\n🟥      🟥\n  🟦  🟦\n    🟥\n    ^",
    "frame8": "    🟦\n  ⬛  🟥\n🟦      🟦\n  🟥  🟥\n    🟦\n    ^",
    }

black_win = {
    "frame1": "    🟦\n  🟥  🟥\n🟦      🟦\n  🟥  ⬛\n    🟦\n    ^",
    "frame2": "    🟥\n  🟦  🟦\n🟥      ⬛\n  🟦  🟦\n    🟥\n    ^",
    "frame3": "    🟦\n  🟥  ⬛\n🟦      🟦\n  🟥  🟥\n    🟦\n    ^",
    "frame4": "    ⬛\n  🟦  🟦\n🟥      🟥\n  🟦  🟦\n    🟥\n    ^",
    "frame5": "    🟦\n  ⬛  🟥\n🟦      🟦\n  🟥  🟥\n    🟦\n    ^",
    "frame6": "    🟥\n  🟦  🟦\n⬛      🟥\n  🟦  🟦\n    🟥\n    ^",
    "frame7": "    🟦\n  🟥  🟥\n🟦      🟦\n  ⬛  🟥\n    🟦\n    ^",
    "frame8": "    🟥\n  🟦  🟦\n🟥      🟥\n  🟦  🟦\n    ⬛\n    ^",
}
#🟥 🟦 ⬛ 

def rouletete():

    if random.randint(1, 6) == 6:
        win = black_win
        win_lose = "black"
    elif random.randint(1,2) == 2:
        win = blue_win
        win_lose = "blue"
    else:
        win = red_win
        win_lose = "red"

    frames = win.values()
    for times in [0.1 ,0.15, 0.2, 0.27, 0.4]: # plays the animation
        for frame in frames:
            clear()
            print(frame)
            time.sleep(times)
    return win_lose # returns what won