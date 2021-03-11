import sys
import requests
import json
from api import Api
from Game import Game


def main():
    if len(sys.argv) < 2:
        print("Too few args")
        return

    api = Api()

    if sys.argv[1] == "-t":
        api.startGame()
    else:
        gameid = int(sys.argv[1])
        api.startGame(gameid)

    print(api.gameid)

    while(1):
        print(api.actionMove('s', 1)["player1"])


    game = Game(1)
    

    

if __name__ == "__main__":
    main()