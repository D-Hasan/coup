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
        self.moves = []
        self.next_player = 0
        self.players = []

        self.player_index = random.randint(0, len(self.players))
        hands = self.deck.get_hands(num_players)
        for i in range(num_players):
            if i == self.player_index:
                player = Player(hands[i], i, self.player_name)
            else:
                player = Player(hands[i], i, self.names[i])
            self.players.append(player)

    def print_status(self):
        # Print players and their status
        print('_________________________________________________________________')
        print('Game Status \n')
        for player in self.players:
            status = 'Alive' if len(player.hand) > 0 else 'Dead'
            hand = []
            for card in player.hand:
                hand.append('Unknown')
            hand += player.revealed
            print('{0:s}: {1:s}, Cards: {2:d}  {3:s}, Coins: {4:d}'.format(player.name,
                                                                status,
                                                                len(player.hand),
                                                                str(hand),
                                                                player.coins))
        print('________________________________________________________________\n')


    def next_turn(self):
        print('Current Player:', self.players[self.next_player].name)
        if self.next_player == self.player_index:
            player = self.players[self.next_player]
            move = player.turn(self.moves, human=True)
        else:
            player = self.players[self.next_player]
            move = player.turn(self.moves)
        
        # if move.challengeable:
        #     for i in range(self.num_players):
        #         if i != self.next_player:
        #             self.players[i].challenge(move)

        self.move_fcn[move.move](self, move)
        print('{:s} did {:s}'.format(self.players[self.next_player].name, move.move))
        
        self.next_player = (self.next_player + 1) % self.num_players
        return move

    def play_game(self):
        end_game = False
        while not end_game:
            move = self.next_turn()
            self.moves.append(move)
            self.print_status()


    def income(self, move):
        self.players[move.player].coins += 1
        return 0

    def foreign_aid(self, move):
        self.players[move.player].coins += 2
        return 0

    def duke(self, move):
        self.players[move.player].coins += 3

    def ambassador(self, move):
        cards = self.deck.get_ambassador()
        if move.player == self.player_index:
            hand = self.players[move.player].hand
            num_hand = len(hand)
            print('Your ambassador has revealed: {:s}'.format(str(cards)))
            print('Your hand is: {:s}'.format(str(hand)))

            new_hand = []
            options = cards + hand
            for i in range(num_hand):
                #TODO: Try Catch for input parsing
                str_options = ''
                for i, item in enumerate(options):
                    str_options += str(item) + ': ' + str(i) + ' | '
                print('Please select a card to keep \n {:s}'.format(str_options))
                sel_option = int(input())
                new_hand.append(options.pop(sel_option))
        else:
            options = self.players[move.player].hand
            new_hand = cards
        self.players[move.player].hand = new_hand
        self.deck.return_ambassador(options)

        return 0


    def assassinate(self, move):
        target = self.players[move.intent[0]]
        target.reveal(move)
        return 0

    def coup(self, move):
        target = self.players[move.intent[0]]
        target.reveal(move)
        return 0

    def steal(self, move):
        player = self.players[move.player]
        target = self.players[move.intent[0]]
        if target.coins < 2:
            player.coins += target.coins
            target.coins = 0
        else:
            player.coins += 2
            target.coins -= 2
        return 0

    move_fcn = {'income': income,
                'foreign aid': foreign_aid,
                'duke': duke,
                'ambassador': ambassador,
                'assassinate': assassinate,
                'coup': coup,
                'steal': steal,
                }
        