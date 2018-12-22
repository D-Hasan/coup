import pytest

from deck import Deck

class TestDeck():
    
    def test_deck_length(self):
        deck = Deck()
        assert len(deck.deck) == 15, "Deck should have 15 cards"
    
    
    def test_deck_hands_2_players(self):
        with pytest.raises(AssertionError):
            deck = Deck()
            num_players = 2
            hands = deck.get_hands(num_players)
            
    def test_deck_hands_7_players(self):
        with pytest.raises(AssertionError):
            deck = Deck()
            num_players = 7
            hands = deck.get_hands(num_players)
            
    def test_deck_hands_quantity(self):
        deck = Deck()
        num_players = 4
        hands = deck.get_hands(num_players)
        assert len(hands) == 4, "Should have dealt 4 hands"
        
    def test_deck_hands_card_quantity(self):
        deck = Deck()
        num_players = 4
        hands = deck.get_hands(num_players)
        for hand in hands:
            assert len(hand) == 2, "Every hand should have 2 cards"
    
    def test_get_ambassador(self):
        deck = Deck()
        ambassador = deck.get_ambassador()
        assert len(ambassador) == 2, "Get ambassador should return 2 cards"
        
    def test_return_ambassador(self):
        deck = Deck()
        ambassador = deck.get_ambassador()
        deck.return_ambassador(ambassador)
        print(len(deck.deck))
        assert len(deck.deck) == 15, "Did not return ambassador cards to deck"
        
    def test_return_ambassador_without_ambassador(self):
        with pytest.raises(AssertionError):
            deck = Deck()
            deck.return_ambassador(['assassin', 'assassin'])
        
    def test_return_ambassador_wrong_card_quantity(self):
        with pytest.raises(AssertionError):
            deck = Deck()
            ambassador = deck.get_ambassador()
            deck.return_ambassador(['assassin'])
    
    def test_return_ambassador_not_list(self):
        with pytest.raises(AssertionError):
            deck = Deck()
            ambassador = deck.get_ambassador()
            deck.return_ambassador(('assassin', 'assassin'))
            
    def test_return_ambassador_not_valid_cards(self):
        with pytest.raises(AssertionError):
            deck = Deck()
            ambassador = deck.get_ambassador()
            deck.return_ambassador(['assassin', 'assassinn'])
        with pytest.raises(AssertionError):
            deck = Deck()
            ambassador = deck.get_ambassador()
            deck.return_ambassador(['assassinn', 'assassin'])'