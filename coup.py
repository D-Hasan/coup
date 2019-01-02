import random

from deck import Deck
from player import Player
from moves import Moves

class CoupGame():
    names = ['Graham', 'Cam', 'Erin', 'Sandy', 'Sam', 'Anna', 'Tim']
    def __init__(self, num_players, name):
        self.player_name = name
        self.num_players = num_players
        self.deck = Deck()
        hands = self.deck.get_hands(num_players)
        
        self.players = {}
        self.player_index = random.randint(0, len(self.players))
        for i in range(num_players):
            if i == self.player_index:
                player = Player(hands[i], self.player_name)
            else:
                player = Player(hands[i], self.names[i])
            self.players[i] = player

        self.player_index = random.randint(0, len(self.players))
        self.moves = Moves()
        self.next_player = 0
        
    def next_turn(self):
        print('Current Player:', self.players[self.next_player].name)
        if self.next_player == self.player_index:
            player = self.players[self.next_player]
            move = player.turn(self.moves, human=True)
        else:
            player = self.players[self.next_player]
            move = player.turn(self.moves)
        
        # if move.challengeable:
        #     for key in self.player.keys():
        #         if key != player_key:
        #             challenge = self.players[key].challenge(move)
        #             
        #             if challenge:
        #                 player.reveal_challenge(move)
        
        self.next_player += 1
        if self.next_player == self.num_players:
            self.next_player = 0
                        
        