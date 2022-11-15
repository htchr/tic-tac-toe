class TicTacToe:
    def __init__(self):
        """
        set up game with board, players, win patterns, and winner
        players are True if played by a human
        """
        self.board = {1: ' ', 2: ' ', 3: ' ', 
                      4: ' ', 5: ' ', 6: ' ',
                      7: ' ', 8: ' ', 9: ' '}
        self.players = {'X': True, 'O': True}
        self.win_patterns = ((1, 2, 3), (4, 5, 6), (7, 8, 9),
                             (1, 4, 7), (2, 5, 8), (3, 6, 9),
                             (1, 5, 9), (3, 5, 7))
        self.winner = None

    def get_board(self):
        """returns: dictionary used as game board"""
        return self.board

    def open_moves(self):
        """returns: dictionary keys with " " as value"""
        moves = []
        for key in self.board.keys():
            if self.board[key] == ' ':
                moves.append(str(key))
        return moves

    def set_player_type(self, player, human):
        self.players[player] = human

    def get_player_type(self, player):
        """returns: boolean if player is human"""
        return self.players[player]

    def other_player(self, player):
        """returns: string O if player is X & vice-versa"""
        for p in self.players.keys():
            if p != player:
                return p

    def update_board(self, player, move):
        self.board[move] = player

    def check_winner(self):
        """returns: None, only works to set self.winner"""
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
        """returns: self.winner ['X won!' / 'O won!' / 'Draw']"""
        return self.winner

    def __str__(self):
        return '{}|{}|{}\n{}|{}|{}\n{}|{}|{}'.format(*(self.board.values()))

