import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_make_empty_board(self):
        self.assertEqual(logic.make_empty_board(), [[None, None, None],
                                                    [None, None, None],
                                                    [None, None, None]])

    def test_update_board(self):
        board1 = [['X', None, 'O'],
                  [None, None, None],
                  [None, 'O', 'X']]
        board2 = [['X', None, 'O'],
                  [None, 'X', None],
                  [None, 'O', 'X']]
        self.assertEqual(logic.update_board('X', board1, (1,1)), board2)

    def test_get_winner(self):
        board = [['X', None, 'O'],
                 [None, 'X', None],
                 [None, 'O', 'X']]
        self.assertEqual(logic.get_winner(board, 'X'), 'X')

    def test_x_to_o(self):
        self.assertEqual(logic.other_player('X'), 'O')

    def test_o_to_x(self):
        self.assertEqual(logic.other_player('O'), 'X')


if __name__ == '__main__':
    unittest.main()

