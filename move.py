class Move():
    moves = ['income', 'foreign aid', 'duke', 'ambassador', 'assassinate', 
             'coup', 'steal']
    
    def __init__(self, move, player):
        self.move = move
        self.player = player
    
    def __print__(self):
        print(self.player, ':', self.move)
        