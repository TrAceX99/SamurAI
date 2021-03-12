import sys
import requests
import json
import time
from random import randrange
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

    game = Game.startGame(api.startGame())
    print(api.gameid)

    while True:
        moves = game.possible_moves()
        move = game.get_move()
        print(move)
        print(moves)
        time.sleep(0.5)
        # rand = randrange(len(moves))
        game.gameInfo = api.doAction(move)


if __name__ == "__main__":
    main()