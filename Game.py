import easyAI



class Game(easyAI.TwoPlayersGame):
    def __init__(self, players) -> None:
        self.players = players 
        self.nplayer = 1 # koji igrac igra, 1 ili 2
        

    def possible_moves(self):
        pass

    def make_move(self, move):
        pass

    def is_over(self):
        pass

    @staticmethod
    def quickSetup():
        return Game([easyAI.Human_Player(), easyAI.AI_Player(easyAI.AI.Negamax(5))])

    @staticmethod
    def startGame(humanPlaysFirst=1, depth=5):
        if humanPlaysFirst == 1:
            return Game([easyAI.Human_Player(), easyAI.AI_Player(easyAI.AI.Negamax(depth))])
        else:
            return Game([easyAI.AI_Player(easyAI.AI.Negamax(depth), easyAI.Human_Player())])

    #def unmake_move(self, move): how to unmake a move (speeds up the AI)