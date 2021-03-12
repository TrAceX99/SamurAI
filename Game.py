import easyAI
from Stack import Stack

class Game(easyAI.TwoPlayersGame):
    def __init__(self, players) -> None:
        self.players = players 
        self.nplayer = 1 # koji igrac igra, 1 ili 2
        self.gameInfo = None
        self.FINITE_STATE_MACHINE = {
            'q' : 'd',
            'w' : 's',
            'e' : 'a',
            'a' : 'e',
            's' : 'w',
            'd' : 'q'
            }

    def _calcTile(self, x, y, dir):
        if dir == 's':
            x += 2
        elif dir == 'w':
            x -= 2
        elif dir == 'd':
            if x % 2 == 1:
                y += 1
            x += 1
        elif dir == 'e':
            if x % 2 == 1:
                y += 1
            x -= 1
        elif dir == 'q':
            if x % 2 == 0:
                y -= 1
            x -= 1
        elif dir == 'a':
            if x % 2 == 0:
                y -= 1
            x += 1
        else:
            return False, None, None

        if x > 26 or x < 0:
            return False, x, y
        if y > 8 or y < 0:
            return False, x, y
        return True, x, y

    def _calcTeleport(self, x, y):
        pass
        

    def possible_moves(self):
        currentPlayerInfo = None
        opponentInfo = None
        if self.player == self.players[0]:
            currentPlayerInfo = self.gameInfo['player1']
            opponentInfo = self.gameInfo["player2"]
        else:
            currentPlayerInfo = self.gameInfo['player2']
            opponentInfo = self.gameInfo["player1"]
        
        mapInfo = self.gameInfo['map']['tiles']
        playerx = currentPlayerInfo["x"]
        playery = currentPlayerInfo["y"]
        playerEnergy = currentPlayerInfo["energy"]

        possibleMoves = []

        #move moves
        x = playerx
        y = playery
        i = 1
        while i <= playerEnergy:
            valid, x, y = self._calcTile(x, y, 'w')
            if not valid or mapInfo[x][y]["ownedByTeam"] != "" or mapInfo[x][y]["tileContent"]["itemType"] == "HOLE":
                break
            possibleMoves.append([0, 'w', i])
            i += 1
        x = playerx
        y = playery
        i = 1
        while i <= playerEnergy:
            valid, x, y = self._calcTile(x, y, 's')
            if not valid or mapInfo[x][y]["ownedByTeam"] != "" or mapInfo[x][y]["tileContent"]["itemType"] == "HOLE":
                break
            possibleMoves.append([0, 's', i])
            i += 1
        x = playerx
        y = playery
        i = 1
        while i <= playerEnergy:
            valid, x, y = self._calcTile(x, y, 'd')
            if not valid or mapInfo[x][y]["ownedByTeam"] != "" or mapInfo[x][y]["tileContent"]["itemType"] == "HOLE":
                break
            possibleMoves.append([0, 'd', i])
            i += 1
        x = playerx
        y = playery
        i = 1
        while i <= playerEnergy:
            valid, x, y = self._calcTile(x, y, 'e')
            if not valid or mapInfo[x][y]["ownedByTeam"] != "" or mapInfo[x][y]["tileContent"]["itemType"] == "HOLE":
                break
            possibleMoves.append([0, 'e', i])
            i += 1
        x = playerx
        y = playery
        i = 1
        while i <= playerEnergy:
            valid, x, y = self._calcTile(x, y, 'q')
            if not valid or mapInfo[x][y]["ownedByTeam"] != "" or mapInfo[x][y]["tileContent"]["itemType"] == "HOLE":
                break
            possibleMoves.append([0, 'q', i])
            i += 1
        x = playerx
        y = playery
        i = 1
        while i <= playerEnergy:
            valid, x, y = self._calcTile(x, y, 'a')
            if not valid or mapInfo[x][y]["ownedByTeam"] != "" or mapInfo[x][y]["tileContent"]["itemType"] == "HOLE":
                break
            possibleMoves.append([0, 'a', i])
            i += 1

        #SkipATurn move
        if currentPlayerInfo["numOfSkipATurnUsed"] < 5:
            possibleMoves.append([1, None, None])

        #StealKoalas move
        opponentx = opponentInfo["x"]
        opponenty = opponentInfo["y"]

        _, x, y = self._calcTile(playerx, playery, 'a')
        if x == opponentx and y == opponenty:
            possibleMoves.append([2, None, None])
        _, x, y = self._calcTile(playerx, playery, 's')
        if x == opponentx and y == opponenty:
            possibleMoves.append([2, None, None])
        _, x, y = self._calcTile(playerx, playery, 'd')
        if x == opponentx and y == opponenty:
            possibleMoves.append([2, None, None])
        _, x, y = self._calcTile(playerx, playery, 'e')
        if x == opponentx and y == opponenty:
            possibleMoves.append([2, None, None])
        _, x, y = self._calcTile(playerx, playery, 'w')
        if x == opponentx and y == opponenty:
            possibleMoves.append([2, None, None])
        _, x, y = self._calcTile(playerx, playery, 'q')
        if x == opponentx and y == opponenty:
            possibleMoves.append([2, None, None])

        # TP
        if len(possibleMoves) == 0:
            possibleMoves.append([3, None, None])

        return possibleMoves

    def make_move(self, move):

        otherPlayerInfo = None
        currentPlayerInfo = None
        if self.player == self.players[0]:
            currentPlayerInfo = self.gameInfo['player1']
            otherPlayerInfo = self.gameInfo['player2']
        else:
            currentPlayerInfo = self.gameInfo['player2']
            otherPlayerInfo = self.gameInfo['player1']
        mapInfo = self.gameInfo['map']['tiles']

        
        if move[0] == 0:
            move.append([])
            for i in range(move[2]):
                _, x, y = self._calcTile(currentPlayerInfo['x'], currentPlayerInfo['y'], move[1])
                value = self.getMoveValue(currentPlayerInfo, mapInfo[x][y]["tileContent"]['itemType'], move[0])

                currentPlayerInfo['x'] = x
                currentPlayerInfo['y'] = y
                currentPlayerInfo['score'] += value
                move[3].append(mapInfo[x][y]["tileContent"]['itemType'])
                mapInfo[x][y]["tileContent"]['itemType'] = "EMPTY"
                mapInfo[x][y]["tileContent"]["numOfItems"] = 0
            mapInfo[x][y]['ownedByTeam'] = currentPlayerInfo['teamName']
        elif move[0] == 1:
            value = self.getMoveValue(currentPlayerInfo, "SKIP", move[0])
            currentPlayerInfo['score'] += value
        elif move[0] == 2:
            value = self.getMoveValue(currentPlayerInfo, "STEAL", move[0])
            currentPlayerInfo['score'] += value
            otherPlayerInfo['score'] -= value
        elif move[0] == 3:
            move.append([])
            value = self.getMoveValue(currentPlayerInfo, "TELEPORT", move[0])
            currentPlayerInfo['score'] += value
            x, y = self._calcTeleport(currentPlayerInfo['x'], currentPlayerInfo['y'])


            move[3].append((currentPlayerInfo['x'], currentPlayerInfo['y']))


            currentPlayerInfo['x'] = x
            currentPlayerInfo['y'] = y
            
            move[3].append(mapInfo[x][y]["tileContent"]['itemType'])
            mapInfo[x][y]["tileContent"]['itemType'] = "EMPTY"
            mapInfo[x][y]["tileContent"]["numOfItems"] = 0
            mapInfo[x][y]['ownedByTeam'] = currentPlayerInfo['teamName']
        return

    def is_over(self):
        
        return False

    def scoring(self):
        currentPlayerInfo = None
        otherPlayerInfo = None
        if self.player == self.players[0]:
            currentPlayerInfo = self.gameInfo['player1']
            otherPlayerInfo = self.gameInfo['player2']
        else:
            currentPlayerInfo = self.gameInfo['player2']
            otherPlayerInfo = self.gameInfo['player1']
        return currentPlayerInfo['score'] - otherPlayerInfo['score']

    @staticmethod
    def quickSetup():
        return Game([easyAI.Human_Player(), easyAI.AI_Player(easyAI.AI.Negamax(5))])

    @staticmethod
    def startGame(gameInfo=None, humanPlaysFirst=False, depth=5):
        game = None
        if humanPlaysFirst:
            game = Game([easyAI.Human_Player(), easyAI.AI_Player(easyAI.AI.Negamax(depth))])
        else:
            game = Game([easyAI.AI_Player(easyAI.AI.Negamax(depth)), easyAI.Human_Player()])
        game.gameInfo = gameInfo
        return game
    

    def unmake_move(self, move):
        currentPlayerInfo = None
        if self.player == self.players[0]:
            currentPlayerInfo = self.gameInfo['player1']
        else:
            currentPlayerInfo = self.gameInfo['player2']

        if move[0] == 0:
            direction = self.FINITE_STATE_MACHINE[move[1]]
            mapInfo = self.gameInfo['map']['tiles']

            for i in range(move[2]):
                itemType = move[3].pop()

                currentPlayerInfo['score'] -= self.getMoveValue(currentPlayerInfo, itemType, move[0])
                mapInfo[currentPlayerInfo['x']][currentPlayerInfo['y']]['ownedByTeam'] = ""
                mapInfo[currentPlayerInfo['x']][currentPlayerInfo['y']]['itemType'] = itemType
                #mapInfo[currentPlayerInfo['x']][currentPlayerInfo['y']]
            
                _, x, y = self._calcTile(currentPlayerInfo['x'], currentPlayerInfo['y'], direction)
                currentPlayerInfo['x'] = x
                currentPlayerInfo['y'] = y
        elif move[0] == 1:
            value = self.getMoveValue(currentPlayerInfo, "SKIP", move[0])
            currentPlayerInfo['score'] -= value
        elif move[0] == 2:
            otherPlayerInfo = None
            if self.player == self.players[0]:
                otherPlayerInfo = self.gameInfo['player2']
            else:
                otherPlayerInfo = self.gameInfo['player1']
            value = self.getMoveValue(currentPlayerInfo, "STEAL", move[0])
            currentPlayerInfo['score'] -= value
            otherPlayerInfo['score'] += value
        elif move[0] == 3:
            mapInfo = self.gameInfo['map']['tiles']
            itemType = move[3].pop()

            currentPlayerInfo['score'] -= self.getMoveValue(currentPlayerInfo, "TELEPORT", move[0])
            mapInfo[currentPlayerInfo['x']][currentPlayerInfo['y']]['ownedByTeam'] = ""
            mapInfo[currentPlayerInfo['x']][currentPlayerInfo['y']]['itemType'] = itemType
            #mapInfo[currentPlayerInfo['x']][currentPlayerInfo['y']]
            x, y = move[3].pop()
            currentPlayerInfo['x'] = x
            currentPlayerInfo['y'] = y
        pass


    def getMoveValue(self, currentPlayerInfo, info, moveType):
        if moveType == 0:
            if info == "ENERGY":
                return 0
            elif info == "KOALA":
                return 50
            elif info == "KOALA_CREW":
                return 1400
        elif moveType == 1:
            return 300
        elif moveType == 2:
            otherPlayerInfo = None
            if self.player == self.players[0]:
                otherPlayerInfo = self.gameInfo['player2']
            else:
                otherPlayerInfo = self.gameInfo['player1']
            value = otherPlayerInfo['gatheredKoalas'] * 150
            return value
        elif moveType == 3:
            return -500
        return 100