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
        best_move = game.get_move()
        if len(moves) == 0:
            game.gameInfo = api.doAction((0, 's', 1))
            print(game.gameInfo['player1'])
        else:
            rand = randrange(len(moves))
            game.gameInfo = api.doAction(best_move)


    
    

    

if __name__ == "__main__":
    main()