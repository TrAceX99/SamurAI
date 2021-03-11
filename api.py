import requests
import json

class Api:
    httpString = "http://147.91.162.72:8080/"
    gameid = 0
    playerid = 713016
    defaultargsString = ""

    def __init__(self):
        pass

    def _send(self, http):
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

        self.defaultargsString += "playerId=" + str(self.playerid) + "&gameId=" + str(self.gameid)

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
