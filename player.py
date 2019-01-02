from move import Move

import random

class Player():
    moves = ['income', 'foreign aid', 'duke', 'ambassador', 'assassinate',
             'coup', 'steal']
    def __init__(self, hand, name):
        self.name = name
        self.hand = hand
        self.influence = 2
        self.coins = 2
        
    def add_coin(self, coins):
        '''coins must be positive'''
        self.coins += coins
        
    def lose_influence(self):
        if self.influence == 1:
            card = self.hand.pop()
        else: 
            card = self.hand.pop(random.randint(0, 1))
        self.influence -= 1
        return card, self.influence
        
    def turn(self, moves, human=False):
        move = 0
        if human:
            while True:
                try:
                    print('Please select your next move:')
                    print('Income: 0')
                    move = int(input())
                    break
                except ValueError:
                    print('Enter a valid move number')
            assert move == 0
        move = Move(self.moves[move], self)
        return move
        
    def challenge(self, move):
        pass
    
    def reveal_challenge(self, move):
        pass

            