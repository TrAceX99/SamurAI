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

    game = Game(1)
    

    print(gameid)

    

if __name__ == "__main__":
    main()