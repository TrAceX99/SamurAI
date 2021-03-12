import requests
import json

class Api:
    httpString = "https://aibg2021.herokuapp.com/"
    gameid = 0
    playerid = 713016
    defaultargsString = ""

    def __init__(self):
        pass

    def _send(self, http):
        req = requests.get(self.httpString + http)
        while req.status_code = 403:
            print("WWWWWWWWWWWW")
            req = requests.get(self.httpString + http)
        response = json.loads(req.text)
        return response


    def startGame(self, gameId = None):
        if gameId == None:
            self.httpString += "train/"
            gamedata = self._send("makeGame?playerId=" + str(self.playerid))
            self.gameid = gamedata["gameId"]
        else:
            self.gameid = gameId
            gamedata = self._send("joinGame?playerId=" + str(self.playerid) + "&gameId=" + str(self.gameid))

        self.defaultargsString += "playerId=" + str(self.playerid) + "&gameId=" + str(self.gameid)
        return gamedata

    def actionSkipATurn(self):
        r = self._send("skipATurn?" + self.defaultargsString)
        return r

    def actionMove(self, dir, dist):
        r = self._send("move?" + self.defaultargsString + "&direction=" + dir + "&distance=" + str(dist))
        return r

    def actionfreeASpot(self, x, y):
        r = self._send("freeASpot?" + self.defaultargsString + "&&x=" + str(x) + "&&y=" + str(y))
        return r
    
    def actionStealKoalas(self):
        r = self._send("stealKoalas?" + self.defaultargsString)
        return r

    def doAction(self, move):
        if move[0] == 0:
            r = self.actionMove(move[1], move[2])
        elif move[0] == 1:
            r = self.actionSkipATurn()
        elif move[0] == 2:
            r = self.actionStealKoalas()
        # Moze biti opasno TODO
        elif move[0] == 3:
            r = self.actionMove('s', 1)
        elif move[0] == 4:
            r = self.actionfreeASpot(move[1], move[2])
        elif move[0] == 5:
            r = self.actionMove(move[1], move[2])
        else:
            return 1
        
        return r
