import pytest
from unittest import mock

from player import Player

class TestPlayer():

    def test_add_coin(self):
        name = 'test'
        hand = mock.Mock()
        player = Player(name, hand)
        player.add_coin(1)
        assert player.coins == 3, 'Player should have 3 coins'

    def test_lose_influence_2_cards(self):
        name = 'test'
        hand = ['contessa', 'contessa']
        player = Player(hand, name)
        player.lose_influence()
        assert player.influence == 1, 'Player should lose influence'
        assert len(player.hand) == 1, 'Player should lose a card'

    def test_lose_influence_1_card(self):
        name = 'test'
        hand = ['captain', 'contessa']
        player = Player(hand, name)
        discard_first = player.lose_influence()[0]
        if discard_first == 'captain':
            player.lose_influence()

        assert player.influence == 0, 'Player should have no influence left'
        assert len(player.hand) == 0, 'Player should have no cards left'

