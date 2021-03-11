import easyAI



class Game(easyAI.TwoPlayersGame):
    def __init__(self, players) -> None:
        self.players = players 
        self.nplayer = 1 # koji igrac igra, 1 ili 2
        self.gameInfo = None

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
        pass

    def is_over(self):
        pass

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