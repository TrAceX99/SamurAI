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

    if sys.argv[1] == "-t":
        game = Game.startGame(api.startGame(), depth=6)
        print(api.gameid)
    else:
        gameid = int(sys.argv[1])
        game = Game.startGame(api.startGame(gameid), depth=6)
        print(game.gameInfo["numOfMove"])

    while game.gameInfo["finished"] == False:
        moves = game.possible_moves()
        move = game.get_move()
        print(move)
        print(moves)
        
        # time.sleep(0.3)
        # rand = randrange(len(moves))
        game.gameInfo = api.doAction(move)

    print(game.gameInfo["winnerTeamName"])


if __name__ == "__main__":
    main()