import typing 
import pandas as pd
from random import choice

class DB:
    def __init__(self) -> None:
        self.path = "./ttt.csv"
        try:
            self.db = pd.read_csv(self.path, index_col=0)
        except FileNotFoundError:
            self.db = pd.DataFrame(columns=[
                                   '1',
                                   '2',
                                   '3',
                                   '4',
                                   '5',
                                   '6',
                                   '7',
                                   '8',
                                   '9',
                                   'PlayerX',
                                   'PlayerO',
                                   'Winner',
                                   'WinnerType',
                                   ])

    def len(self) -> int:
        """returns the number of rows in db"""
        return len(self.db)

    def write_move(self, GameId: int, move: int, player: str) -> None:
        """record a move to the game's row in the data base"""
        self.db.at[GameId, move] = player

    def write_player(self, GameId: int, symbol: str, player_type: str) -> None:
        """record what type of player in db"""
        self.db.at[GameId, 'Player'+symbol] = player_type

    def write_winner(self, GameId: int, winner: str) -> None:
        """record the winner of the game"""
        self.db.at[GameId, 'Winner'] = winner

    def write_winner_type(self, GameId: int, player_type: str) -> None:
        """record the type of player that won the game"""
        self.db.at[GameId, 'WinnerType'] = player_type

    def save(self) -> None:
        """save the db back to the csv"""
        self.db.to_csv(self.path)
    
    def stats(self, board: dict, winner: str) -> str:
        """returns a string of game db stats"""
        finished_games = self.db[self.db['WinnerType'].notna()]
        # how often the winning player's symbol wins
        n_wins = len(self.db[self.db['Winner'] == winner])
        win_percent = int((n_wins / len(finished_games)) * 100)
        if winner == 'D':
            win_percent_str = f'This game was a draw, the game ends in a draw {win_percent}% of the time.\n'
        else:
           win_percent_str = f'{winner} wins {win_percent}% of the time\n'
        # the number of moves made in a game vs the avg number of moves
        n_moves = 0
        for k in board.values():
            if k != ' ': n_moves += 1
        n_nulls = finished_games[['1', '2', '3', '4', '5', '6', '7', '8', '9']].isnull().sum().sum()
        avg_moves = round((len(finished_games) * 9 - n_nulls) / len(finished_games))
        moves_str = f'This game took {n_moves} moves\nthe average game takes {avg_moves} moves\n'
        return win_percent_str + moves_str

    def remove_last_row(self) -> None:
        """remove the last row in the db to clear residules from unit tests"""
        self.db = self.db.drop(len(self.db) - 1)
        self.save()

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
        self.db = DB()
        self.GameId = self.db.len()
        self.board = {1: ' ', 2: ' ', 3: ' ', 
                      4: ' ', 5: ' ', 6: ' ',
                      7: ' ', 8: ' ', 9: ' '}
        self.win_patterns = ((1, 2, 3), (4, 5, 6), (7, 8, 9),
                             (1, 4, 7), (2, 5, 8), (3, 6, 9),
                             (1, 5, 9), (3, 5, 7))
        self.players = {'X': None, 'O': None}
        self.player = 'X'
        self.winner = None

    def get_db(self) -> DB:
        """expose db to save when user quits"""
        return self.db

    def get_board(self) -> dict:
        """returns: dictionary used as game board"""
        return self.board

    def open_moves(self) -> list:
        """returns: dictionary keys with ' ' as value"""
        moves = []
        for key in self.board.keys():
            if self.board[key] == ' ':
                moves.append(str(key))
        return moves

    def set_player_type(self, symbol: str, player: Player) -> None:
        self.db.write_player(self.GameId, symbol, type(player).__name__)
        self.players[symbol] = player

    def get_player(self) -> Player:
        """returns the current player object"""
        return self.players[self.player]

    def switch_player(self) -> None:
        """returns: string O if player is X & vice-versa"""
        for key in self.players.keys():
            if key != self.player:
                self.player = key
                return

    def update_board(self, move: str) -> None:
        self.db.write_move(self.GameId, move, self.player)
        self.board[int(move)] = self.player

    def check_winner(self) -> None:
        """returns: None, only works to set self.winner"""
        for key in self.players.keys():
            for pattern in self.win_patterns:
                test = []
                for spot in pattern:
                    test.append(self.board[spot])
                    if test == [key, key, key]:
                        self.winner = f'{key} won!'
        if self.open_moves() == [] and self.winner == None:
            self.winner = 'Draw'
            self.db.write_winner(self.GameId, self.winner[:1])
            self.db.save()
        elif self.winner != None:
            self.db.write_winner(self.GameId, self.winner[:1])
            self.db.write_winner_type(self.GameId, type(self.players[self.winner[:1]]).__name__)
            self.db.save()

    def get_winner(self) -> str:
        """returns: self.winner ['X won!' / 'O won!' / 'Draw']"""
        return self.winner
    
    def post_game_stats(self) -> str:
        """return a series of game stats"""
        return self.db.stats(self.board, self.winner[:1])

    def __str__(self) -> str:
        """reformat how this class is printed"""
        return '{}|{}|{}\n{}|{}|{}\n{}|{}|{}'.format(*(self.board.values()))

class Bot(Player):
    def move(self, ttt: TicTacToe) -> None:
        """generate random play from bot"""
        move = choice(ttt.open_moves())
        ttt.update_board(move)

