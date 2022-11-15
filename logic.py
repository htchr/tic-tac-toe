class TicTacToe:
    def __init__(self):
        self.board = {1: ' ', 2: ' ', 3: ' ', 
                      4: ' ', 5: ' ', 6: ' ',
                      7: ' ', 8: ' ', 9: ' '}
        self.players = {'X': True, 'O': True}
        self.win_patterns = ((1, 2, 3), (4, 5, 6), (7, 8, 9),
                             (1, 4, 7), (2, 5, 8), (3, 6, 9),
                             (1, 5, 9), (3, 5, 7))
        self.winner = None

    def open_moves(self):
        moves = []
        for key in self.board.keys():
            if self.board[key] == ' ':
                moves.append(str(key))
        return moves

    def set_player_type(self, player, human):
        self.players[player] = human

    def get_player_type(self, player):
        return self.players[player]

    def other_player(self, player):
        for p in self.players.keys():
            if p != player:
                return p

    def update_board(self, player, move):
        self.board[move] = player

    def check_winner(self):
        for player in self.players.keys():
            for pattern in self.win_patterns:
                test = []
                for spot in pattern:
                    test.append(self.board[spot])
                    if test == [player, player, player]:
                        self.winner = f'{player} won!'
                        return
        if self.open_moves() == []:
            self.winner = 'Draw'
        return

    def get_winner(self):
        return self.winner

    def __str__(self):
        return '{}|{}|{}\n{}|{}|{}\n{}|{}|{}'.format(*(self.board.values()))

