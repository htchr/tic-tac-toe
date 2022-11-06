# this file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    """returns a new board"""
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]


def update_board(player, board, move):
    """set a cell of the board to the player"""
    board[move[0]][move[1]] = player
    return board


def get_winner(board, player):
    """ loop through all possible win patterns to find a winner
    returns boolean if win is found"""
    patterns = (((0,0), (0,1), (0,2)), # row win patterns
                ((1,0), (1,1), (1,2)),
                ((2,0), (2,1), (2,2)),
                ((0,0), (1,0), (2,0)), # column win patterns
                ((0,1), (1,1), (2,1)),
                ((0,2), (1,2), (2,2)),
                ((0,0), (1,1), (2,2)), # diagonal win patterns
                ((0,2), (1,1), (2,0)))
    for pattern in patterns:
        test = []
        for coordinates in pattern:
            test.append(board[coordinates[0]][coordinates[1]])
        if test == [player, player, player]:
            return player
    return None


def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == "X":
        return "O"
    else:
        return "X"

