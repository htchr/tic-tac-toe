import unittest
import logic

class TestLogic(unittest.TestCase):

    def setUp(self):
        self.ttt = logic.TicTacToe()

    def test_get_board(self):
        self.assertEqual(self.ttt.get_board(), {1: ' ', 2: ' ', 3: ' ', 
                                                4: ' ', 5: ' ', 6: ' ',
                                                7: ' ', 8: ' ', 9: ' '})

    def test_open_moves(self):
        self.assertEquals(self.ttt.open_moves(), ['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    def test_set_get_player_type(self):
        self.ttt.set_player_type('X', False)
        self.assertEquals(isinstance(self.ttt.get_player(), logic.Bot), True)

    def test_switch_player(self):
        self.ttt.switch_player()
        self.ttt.set_player_type('O', False)
        self.assertEqual(str(self.ttt.get_player()), 'O')

    def test_update_board(self):
        new_board = {1: 'X', 2: ' ', 3: ' ', 
                     4: ' ', 5: ' ', 6: ' ',
                     7: ' ', 8: ' ', 9: ' '}
        self.ttt.update_board(1)
        self.assertEqual(self.ttt.get_board(), new_board)

    def test_check_get_winner(self):
        self.ttt.update_board(1)
        self.ttt.update_board(2)
        self.ttt.update_board(3)
        self.ttt.check_winner()
        self.assertEqual(self.ttt.get_winner(), 'X won!')
    
if __name__ == '__main__':
    unittest.main()

