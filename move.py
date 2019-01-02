class Move():
    moves = ['income', 'foreign aid', 'duke', 'ambassador', 'assassinate', 
             'coup', 'steal']
    
    def __init__(self, move, player):
        assert move in self.moves, "Not a valid move"
        self.move = move
        self.player = player
        if move == 'income' or move == 'coup':
            self.challengeable = False
        else: 
            self.challengeable = True
            
    def print (self):
        print(self.player.name, ':', self.move)
        