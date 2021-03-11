import easyAI
from Stack import Stack

class Game(easyAI.TwoPlayersGame):
    def __init__(self, players) -> None:
        self.players = players 
        self.nplayer = 1 # koji igrac igra, 1 ili 2
        self.gameInfo = None
        self.stack = Stack()

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
            return None, None

        if x > 8 or x < 0:
            return None, None
        if y > 26 or y < 0:
            return None, None
        return x, y
        

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
            x, y = self._calcTile(x, y, 's')
            if x == None or mapInfo[x][y]["ownedByTeam"] != "" or mapInfo[x][y]["tileContent"]["itemType"] == "HOLE":
                break
            possibleMoves.append((0, 's', i))
            i += 1
        x = playerx
        y = playery
        i = 1
        while i <= playerEnergy:
            x, y = self._calcTile(x, y, 'w')
            if x == None or mapInfo[x][y]["ownedByTeam"] != "" or mapInfo[x][y]["tileContent"]["itemType"] == "HOLE":
                break
            possibleMoves.append((0, 'w', i))
            i += 1
        x = playerx
        y = playery
        i = 1
        while i <= playerEnergy:
            x, y = self._calcTile(x, y, 'd')
            if x == None or mapInfo[x][y]["ownedByTeam"] != "" or mapInfo[x][y]["tileContent"]["itemType"] == "HOLE":
                break
            possibleMoves.append((0, 'd', i))
            i += 1
        x = playerx
        y = playery
        i = 1
        while i <= playerEnergy:
            x, y = self._calcTile(x, y, 'e')
            if x == None or mapInfo[x][y]["ownedByTeam"] != "" or mapInfo[x][y]["tileContent"]["itemType"] == "HOLE":
                break
            possibleMoves.append((0, 'e', i))
            i += 1
        x = playerx
        y = playery
        i = 1
        while i <= playerEnergy:
            x, y = self._calcTile(x, y, 'q')
            if x == None or mapInfo[x][y]["ownedByTeam"] != "" or mapInfo[x][y]["tileContent"]["itemType"] == "HOLE":
                break
            possibleMoves.append((0, 'q', i))
            i += 1
        x = playerx
        y = playery
        i = 1
        while i <= playerEnergy:
            x, y = self._calcTile(x, y, 'a')
            if x == None or mapInfo[x][y]["ownedByTeam"] != "" or mapInfo[x][y]["tileContent"]["itemType"] == "HOLE":
                break
            possibleMoves.append((0, 'a', i))
            i += 1

        #SkipATurn move
        if currentPlayerInfo["numOfSkipATurnUsed"] < 5:
            possibleMoves.append((1, None, None))

        #StealKoalas move
        opponentx = opponentInfo["x"]
        opponenty = opponentInfo["y"]

        x, y = self._calcTile(playerx, playery, 'a')
        if x == opponentx and y == opponenty:
            possibleMoves.append((2, None, None))
        x, y = self._calcTile(playerx, playery, 's')
        if x == opponentx and y == opponenty:
            possibleMoves.append((2, None, None))
        x, y = self._calcTile(playerx, playery, 'd')
        if x == opponentx and y == opponenty:
            possibleMoves.append((2, None, None))
        x, y = self._calcTile(playerx, playery, 'e')
        if x == opponentx and y == opponenty:
            possibleMoves.append((2, None, None))
        x, y = self._calcTile(playerx, playery, 'w')
        if x == opponentx and y == opponenty:
            possibleMoves.append((2, None, None))
        x, y = self._calcTile(playerx, playery, 'q')
        if x == opponentx and y == opponenty:
            possibleMoves.append((2, None, None))

        return possibleMoves

    def make_move(self, move):

        self.stack.push(move)
        if move[0] == 0:
            
            pass
        return

    def is_over(self):
        pass

    def scoring(self):
        currentPlayerInfo = None
        if self.player == self.players[0]:
            currentPlayerInfo = self.gameInfo['player1']
        else:
            currentPlayerInfo = self.gameInfo['player2']
        return currentPlayerInfo['score']

    @staticmethod
    def quickSetup():
        return Game([easyAI.Human_Player(), easyAI.AI_Player(easyAI.AI.Negamax(5))])

    @staticmethod
    def startGame(gameInfo=None, humanPlaysFirst=1, depth=5):
        game = None
        if humanPlaysFirst == 1:
            game = Game([easyAI.Human_Player(), easyAI.AI_Player(easyAI.AI.Negamax(depth))])
        else:
            game = Game([easyAI.AI_Player(easyAI.AI.Negamax(depth), easyAI.Human_Player())])
        game.gameInfo = gameInfo
        return game
    
    

    #def unmake_move(self, move): how to unmake a move (speeds up the AI)