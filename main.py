import sys
import requests
import json
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

    print(api.gameid)
    game = Game.startGame(api.startGame())

    while True:
        moves = game.possible_moves()
        print(moves)
        rand = randrange(len(moves))
        game.gameInfo = api.doAction(moves[rand])


    
    

    

if __name__ == "__main__":
    main()