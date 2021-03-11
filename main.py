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

    # if sys.argv[1] == "-t":
    #     api.startGame()
    # else:
    #     gameid = int(sys.argv[1])
    #     api.startGame(gameid)

    print(api.gameid)
    game = Game.startGame(api.startGame())

    gameInfo = api.actionMove('s', 1)

    print(game.possible_moves())
    

    

if __name__ == "__main__":
    main()