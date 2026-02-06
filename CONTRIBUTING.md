# Contributing and Aiding with Reel Estate Plus

Thank you for the attention, and ideas you will contribute. This is a python pure project with a modular structure.

## Getting started!

1. obtain the repo i.e. Forking the repo and cloning your version of the repo

2. downloading the dependencies 

```
pip install -r requirements.txt
```
3. compiling with pyinstaller through this command: 

```
pyinstaller --onefile --name=ReelEstatePlus --paths=. REP/core/player_init.py --clean
```
4. run and test | naming yourself kondike gives access to the dev console

## project structure

- constants has Cmds.json, lore.json, and save_stuff. Cmds is all the commands for the dev console. lore.json has all the dialogue, and save_stuff has the information needed for a new save file to be made

- core has the player_init which is splash and play screen, analysis which is for checking the choices from player_init, and Hub.py which is the main game loop

- Modules has everything else. including the save/load functions. there is a load and json_load. json_load is for lore NOT saves.

Please use the existing save/load systems already implemented.

If you find a bug please test with multiple save files before reporting.

## How to Contribute
 **Bug report**: Please Include python version, Steps to reproduce, and save file state if relevant to the bug at hand

 **requesting features**: Open a issue and discuss it there. I will look.

 **No pull requests**: Thanks, but not needed. I would like to maintain Reel Estate Plus by myself. feel free to do pull requests with other forks.

 ## Questions
 open a discussion or reach out via discord (kondike_barr)