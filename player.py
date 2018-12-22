import random

class Player():
    
    def __init__(self, hand):
        self.hand = hand
        self.influence = 2
        self.coins = 2
        
    def add_coin(self, coins):
        self.coins += coins
        
    def lose_influence(self):
        if self.influence == 1:
            card = self.hand.pop()
        else: 
            card = self.hand[random.randint(0, 1)]
        self.influence -= 1
        return card, self.influence

            