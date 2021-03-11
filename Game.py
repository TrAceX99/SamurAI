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
        pass
        

    def possible_moves(self):
        currentPlayerInfo = None
        if self.player == self.players[0]:
            currentPlayerInfo = self.gameInfo['player1']
        else:
            currentPlayerInfo = self.gameInfo['player2']
        mapInfo = self.gameInfo['map']['tiles']

        possibleMoves = []

    def make_move(self, move):


        currentPlayerInfo = None
        if self.player == self.players[0]:
            currentPlayerInfo = self.gameInfo['player1']
        else:
            currentPlayerInfo = self.gameInfo['player2']
        mapInfo = self.gameInfo['map']['tiles']

        move.info = []
        if move[0] == 0:
            for i in range(move[2]):
                x, y = self._calcTile(currentPlayerInfo['x'], currentPlayerInfo['y'], move[1])
                currentPlayerInfo['x'] = x
                currentPlayerInfo['y'] = y
                value = self.getMoveValue(currentPlayerInfo, mapInfo[x][y]["tileContent"]['itemType'])
                currentPlayerInfo['score'] += value
                move.info(mapInfo[x][y]["tileContent"]['itemType'])
                mapInfo[x][y]["tileContent"]['itemType'] = "EMPTY"
                mapInfo[x][y]["tileContent"]["numOfItems"] = 0
            mapInfo[x][y]['ownedByTeam'] = currentPlayerInfo['teamName']
        return

    def is_over(self):
        pass

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
    def startGame(gameInfo=None, humanPlaysFirst=1, depth=5):
        game = None
        if humanPlaysFirst == 1:
            game = Game([easyAI.Human_Player(), easyAI.AI_Player(easyAI.AI.Negamax(depth))])
        else:
            game = Game([easyAI.AI_Player(easyAI.AI.Negamax(depth), easyAI.Human_Player())])
        game.gameInfo = gameInfo
        return game
    
    def _calcTile(self, x, y, dir):
        pass

    def unmake_move(self, move):

        direction = self.FINITE_STATE_MACHINE[move[1]]
        mapInfo = self.gameInfo['map']['tiles']

        currentPlayerInfo = None
        if self.player == self.players[0]:
            currentPlayerInfo = self.gameInfo['player1']
        else:
            currentPlayerInfo = self.gameInfo['player2']


        itemType = move.info.pop()

        currentPlayerInfo['score'] -= self.getMoveValue(currentPlayerInfo, itemType)
        mapInfo[currentPlayerInfo['x']][currentPlayerInfo['y']]['ownedByTeam'] = ""
        mapInfo[currentPlayerInfo['x']][currentPlayerInfo['y']]['itemType'] = move.info.pop()
        #mapInfo[currentPlayerInfo['x']][currentPlayerInfo['y']]
        
        x, y = self._calcTile(currentPlayerInfo['x'], currentPlayerInfo['y'], direction)
        currentPlayerInfo['x'] = x
        currentPlayerInfo['y'] = y

        pass