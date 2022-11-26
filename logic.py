import typing 
from random import choice

class Player:
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol

    def __str__(self) -> None:
        return f'{self.symbol}'

class TicTacToe:
    def __init__(self) -> None:
        """
        set up game with board, players, win patterns, and winner
        players are True if played by a human
        """
        self.board = {1: ' ', 2: ' ', 3: ' ', 
                      4: ' ', 5: ' ', 6: ' ',
                      7: ' ', 8: ' ', 9: ' '}
        self.player = 'X'
        self.players = {'X': None, 'O': None}
        self.win_patterns = ((1, 2, 3), (4, 5, 6), (7, 8, 9),
                             (1, 4, 7), (2, 5, 8), (3, 6, 9),
                             (1, 5, 9), (3, 5, 7))
        self.winner = None

    def get_board(self) -> dict:
        """returns: dictionary used as game board"""
        return self.board

    def open_moves(self) -> list:
        """returns: dictionary keys with " " as value"""
        moves = []
        for key in self.board.keys():
            if self.board[key] == ' ':
                moves.append(str(key))
        return moves

    def set_player_type(self, symbol: str, player: Player) -> None:
        self.players[symbol] = player

    def get_player(self) -> Player:
        """returns: boolean if player is human"""
        return self.players[self.player]

    def switch_player(self) -> None:
        """returns: string O if player is X & vice-versa"""
        for key in self.players.keys():
            if key != self.player:
                self.player = key
                return

    def update_board(self, move: int) -> None:
        self.board[move] = self.player

    def check_winner(self) -> None:
        """returns: None, only works to set self.winner"""
        for key in self.players.keys():
            for pattern in self.win_patterns:
                test = []
                for spot in pattern:
                    test.append(self.board[spot])
                    if test == [key, key, key]:
                        self.winner = f'{key} won!'
                        return
        if self.open_moves() == []:
            self.winner = 'Draw'

    def get_winner(self) -> str:
        """returns: self.winner ['X won!' / 'O won!' / 'Draw']"""
        return self.winner

    def __str__(self) -> str:
        """reformat how this class is printed"""
        return '{}|{}|{}\n{}|{}|{}\n{}|{}|{}'.format(*(self.board.values()))

class Bot(Player):
    def move(self, ttt: TicTacToe) -> None:
        """
        generate random play from bot
        ttt: TicTacToe instance
        player: string 'X' or 'O'
        returns: None
        """
        moves = ttt.open_moves()
        ttt.update_board(int(choice(moves)))

