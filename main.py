import sys
import requests
import json


def main():
    if len(sys.argv) < 2:
        print("Too few args")
        return


    if sys.argv[1] == "-d":
        r = requests.get(httpString + "makeGame?playerId=" + str(playerid))
        gamedata = json.loads(r.text)
        gameid = gamedata["gameId"]
    else:
        gameid = int(sys.argv[1])

    print(gameid)

    

if __name__ == "__main__":
    main()