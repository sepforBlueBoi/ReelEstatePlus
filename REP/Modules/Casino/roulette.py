import time
import os, sys
import random


def clear():
    sys.stdout.write("\033[H\033[2J\033[3J")

red_win = {
    "frame1": "    \U0001F7E6\n  \U0001F7E5  \U0001F7E5\n\U0001F7E6      \U0001F7E6\n  \U00002B1B  \U0001F7E5\n    \U0001F7E6\n    ^",
    "frame2": "    \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n\U0001F7E5      \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n    \U00002B1B\n    ^",
    "frame3": "    \U0001F7E6\n  \U0001F7E5  \U0001F7E5\n\U0001F7E6      \U0001F7E6\n  \U0001F7E5  \U00002B1B\n    \U0001F7E6\n    ^",
    "frame4": "    \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n\U0001F7E5      \U00002B1B\n  \U0001F7E6  \U0001F7E6\n    \U0001F7E5\n    ^",
    "frame5": "    \U0001F7E6\n  \U0001F7E5  \U00002B1B\n\U0001F7E6      \U0001F7E6\n  \U0001F7E5  \U0001F7E5\n    \U0001F7E6\n    ^",
    "frame6": "    \U00002B1B\n  \U0001F7E6  \U0001F7E6\n\U0001F7E5      \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n    \U0001F7E5\n    ^",
    "frame7": "    \U0001F7E6\n  \U00002B1B  \U0001F7E5\n\U0001F7E6      \U0001F7E6\n  \U0001F7E5  \U0001F7E5\n    \U0001F7E6\n    ^",
    "frame8": "    \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n\U00002B1B      \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n    \U0001F7E5\n    ^",
}
 
blue_win = {
    "frame1": "    \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n\U00002B1B      \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n    \U0001F7E5\n    ^",
    "frame2": "    \U0001F7E6\n  \U0001F7E5  \U0001F7E5\n\U0001F7E6      \U0001F7E6\n  \U00002B1B  \U0001F7E5\n    \U0001F7E6\n    ^",
    "frame3": "    \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n\U0001F7E5      \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n    \U00002B1B\n    ^",
    "frame4": "    \U0001F7E6\n  \U0001F7E5  \U0001F7E5\n\U0001F7E6      \U0001F7E6\n  \U0001F7E5  \U00002B1B\n    \U0001F7E6\n    ^",
    "frame5": "    \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n\U0001F7E5      \U00002B1B\n  \U0001F7E6  \U0001F7E6\n    \U0001F7E5\n    ^",
    "frame6": "    \U0001F7E6\n  \U0001F7E5  \U00002B1B\n\U0001F7E6      \U0001F7E6\n  \U0001F7E5  \U0001F7E5\n    \U0001F7E6\n    ^",
    "frame7": "    \U00002B1B\n  \U0001F7E6  \U0001F7E6\n\U0001F7E5      \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n    \U0001F7E5\n    ^",
    "frame8": "    \U0001F7E6\n  \U00002B1B  \U0001F7E5\n\U0001F7E6      \U0001F7E6\n  \U0001F7E5  \U0001F7E5\n    \U0001F7E6\n    ^",
    }
 
black_win = {
    "frame1": "    \U0001F7E6\n  \U0001F7E5  \U0001F7E5\n\U0001F7E6      \U0001F7E6\n  \U0001F7E5  \U00002B1B\n    \U0001F7E6\n    ^",
    "frame2": "    \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n\U0001F7E5      \U00002B1B\n  \U0001F7E6  \U0001F7E6\n    \U0001F7E5\n    ^",
    "frame3": "    \U0001F7E6\n  \U0001F7E5  \U00002B1B\n\U0001F7E6      \U0001F7E6\n  \U0001F7E5  \U0001F7E5\n    \U0001F7E6\n    ^",
    "frame4": "    \U00002B1B\n  \U0001F7E6  \U0001F7E6\n\U0001F7E5      \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n    \U0001F7E5\n    ^",
    "frame5": "    \U0001F7E6\n  \U00002B1B  \U0001F7E5\n\U0001F7E6      \U0001F7E6\n  \U0001F7E5  \U0001F7E5\n    \U0001F7E6\n    ^",
    "frame6": "    \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n\U00002B1B      \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n    \U0001F7E5\n    ^",
    "frame7": "    \U0001F7E6\n  \U0001F7E5  \U0001F7E5\n\U0001F7E6      \U0001F7E6\n  \U00002B1B  \U0001F7E5\n    \U0001F7E6\n    ^",
    "frame8": "    \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n\U0001F7E5      \U0001F7E5\n  \U0001F7E6  \U0001F7E6\n    \U00002B1B\n    ^",
}


#\U0001F7E5[RED] \U0001F7E6[BLUE] \U00002B1B[RED]
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
