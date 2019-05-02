from move import Move

import random
move_string = 'Income: 0, Foreign Aid: 1, Duke: 2, Ambassador: 3, Assassinate: 4, Coup: 5, Steal: 6'
class Player():
    moves = ['income', 'foreign aid', 'duke', 'ambassador', 'assassinate',
             'coup', 'steal']
    def __init__(self, hand, num, name):
        self.name = name
        self.num = num
        self.hand = hand
        self.revealed = []
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
            valid_move = False
            while not valid_move:
                try:
                    print('Please select your next move:')
                    print(move_string)
                    move = int(input())
                    valid_move = self.valid_move(move)
                except ValueError:
                    print('Enter a valid move number')
            # assert move == 0
        move = Move(self.moves[move], self.num)
        return move
        
    def challenge(self, move):
        pass
    
    def reveal_challenge(self, move):
        pass

    def reveal(self, move):
        pass

    def valid_move(self, move):
        if move < 0 or move > 6:
            return False
        elif self.moves[move] == 'coup' and self.coins < 7:
            return False
        elif self.moves[move] == 'assassinate' and self.coins < 3:
            return False
        else:
            return True

            