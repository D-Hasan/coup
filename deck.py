from random import shuffle

class Deck:
    cards = ['ambassador', 'duke', 'assassin', 'contessa', 'captain']
    ambassador = False

    def __init__(self):
        self.deck = [card for card in self.cards] * 3
        shuffle(self.deck)
    
    def get_hands(self, num_players):
        assert(num_players <= 6 and num_players >=3), "Number of players has to be between 3 and 6"
        
        hands = []
        for i in range(num_players):
            hand = []
            hand.append(self.deck.pop(-1))
            hand.append(self.deck.pop(-1))
            
            hands.append(hand)
        
        return hands

    def swap_card(self, card):
        self.deck.append(card)
        shuffle(self.deck)
        return self.deck.pop(-1)

    def get_ambassador(self):
        cards = [self.deck.pop(-1), self.deck.pop(-1)]
        self.ambassador = True
        return cards
        
    def return_ambassador(self, cards):
        assert type(cards) == list, "Return ambassador takes a list of cards"
        assert (len(cards) == 2), "Did not return 2 cards to deck"
        assert self.ambassador == True, "No one has called ambassador"
        for card in cards:
            assert card in self.cards, "Card is not a valid card"
        
        self.deck += cards
        shuffle(self.deck)
        
    
        
    