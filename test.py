import unittest
from unittest.mock import patch
import logic
from board import Board
from player import Player, Bot
from game import Game


class TestLogic(unittest.TestCase):

    def test_make_empty_board(self):
        expected = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(logic.make_empty_board(), expected)

    def test_get_winner_horizontal(self):
        board = [
            ['X', 'X', 'X'],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
        
    def test_get_winner_vertical(self):
        board = [
            ['O', None, None],
            ['O', None, None],
            ['O', None, None],
        ]
        self.assertEqual(logic.get_winner(board), 'O')
        
    def test_get_winner_diagonal(self):
        board = [
            ['X', None, None],
            [None, 'X', None],
            [None, None, 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def test_other_player(self):
        self.assertEqual(logic.other_player('X'), 'O')
        self.assertEqual(logic.other_player('O'), 'X')

class TestBoard(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()

    def test_initialization(self):
        self.assertEqual(self.board.board, [[None]*3 for _ in range(3)])

    def test_is_full_false(self):
        self.assertFalse(self.board.is_full())

    def test_is_full_true(self):
        self.board.board = [['X', 'O', 'X']] * 3
        self.assertTrue(self.board.is_full())

    def test_get_winner_no_winner(self):
        self.assertIsNone(self.board.get_winner())

    def test_get_winner_row_winner(self):
        self.board.board = [['X', 'X', 'X'], [None, None, None], [None, None, None]]
        self.assertEqual(self.board.get_winner(), 'X')

    def test_make_move(self):
        self.assertTrue(self.board.make_move('X', 0, 0))
        self.assertEqual(self.board.board[0][0], 'X')
        self.assertFalse(self.board.make_move('X', 0, 0))

    def test_display(self):
        try:
            self.board.display()
        except Exception as e:
            self.fail(f"Display method failed with exception {e}")



class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player('X')

    def test_init(self):
        self.assertEqual(self.player.symbol, 'X')

    @patch('builtins.input', return_value='1 1')
    def test_get_move_valid(self, mock_input):
        board = Board()
        move = self.player.get_move(board)
        self.assertEqual(move, (0, 0))

class TestBot(unittest.TestCase):

    def setUp(self):
        self.bot = Bot('O', 1)

    def test_init(self):
        self.assertEqual(self.bot.symbol, 'O')
        self.assertEqual(self.bot.difficulty, 1)

    def test_get_move_easy(self):
        board = Board()
        move = self.bot.get_move(board)
        self.assertIn(move, [(i, j) for i in range(3) for j in range(3) if board.board[i][j] is None])

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.game = Game(self.player1, self.player2)

    def test_initialization(self):
        self.assertIsInstance(self.game.board, Board)
        self.assertEqual(self.game.players, [self.player1, self.player2])
        self.assertEqual(self.game.current_player_index, 0)

    def test_switch_player(self):
        self.game.switch_player()
        self.assertEqual(self.game.current_player_index, 1)
        self.game.switch_player()
        self.assertEqual(self.game.current_player_index, 0)

    @patch('player.Player.get_move', return_value=(0, 0))
    def test_play_turn(self, mock_get_move):
        self.game.play_turn()
        self.assertEqual(self.game.board.board[0][0], 'X')
        mock_get_move.assert_called_once()

    def test_check_for_winner_no_winner(self):
        winner = self.game.check_for_winner()
        self.assertIsNone(winner)
    
    def test_check_for_winner_row_winner(self):
        self.game.board.board = [['X', 'X', 'X'], [None, None, None], [None, None, None]]
        winner = self.game.check_for_winner()
        self.assertEqual(winner, 'X')

    def test_check_for_winner_column_winner(self):
        self.game.board.board = [['O', None, None], ['O', None, None], ['O', None, None]]
        winner = self.game.check_for_winner()
        self.assertEqual(winner, 'O')

    def test_check_for_winner_diagonal_winner(self):
        self.game.board.board = [['X', None, None], [None, 'X', None], [None, None, 'X']]
        winner = self.game.check_for_winner()
        self.assertEqual(winner, 'X')


if __name__ == '__main__':
    unittest.main()
