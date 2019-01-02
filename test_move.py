import pytest
from unittest import mock
from move import Move

class TestMove():

    def test_legal_move(self):
        player = mock.Mock()
        moves = ['income', 'foreign aid', 'duke', 'ambassador', 'assassinate',
                 'coup', 'steal']
        for move in moves:
            test_move = Move(move, player)
            assert test_move.move == move, "The move is not assigned correctly"

    def test_illegal_move(self):
        player = mock.Mock()
        with pytest.raises(AssertionError):
            test_move = Move('block', player)

    def test_print_move(self, capsys):
        player = mock.Mock()
        player.name = 'Jeff'
        test_move = Move('income', player)
        test_move.print()
        out, err = capsys.readouterr()
        assert out == 'Jeff : income\n'

