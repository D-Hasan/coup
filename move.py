moves = ['income', 'foreign aid', 'duke', 'ambassador', 'assassinate',
             'coup', 'steal']
intents = {'income': ['get', 1],
           'foreign aid': ['get', 2],
           'duke': ['get', 3],
           'ambassador': ['cards', -1],
           'assassinate': ['kill', -1],
           'coup': ['kill', -1],
           'steal': ['take', 2]}
class Move():

    # Result: (
    # resulting_player,
    # affected attribute (card(s) or money),
    # effect(card(s) revealed or money gained/lost)
    # )
    def __init__(self, move, player, target=-1):
        assert move in moves, "Not a valid move"
        self.move = move
        self.player = player
        self.intent = (target, intents[move][0], intents[move][1] )
        if move == 'income' or move == 'coup':
            self.challengeable = False
        else: 
            self.challengeable = True
        self.challenge = -1     #No one challenged by default
        self.counter_move = -1  #Target did not counter by default
        self.counter_challenge = -1     #Did not counter challenge by default
        self.result = (-1, -1, -1)      #Encoded to no outcome yet

    def print (self):
        print(self.player.name, ':', self.move)
        