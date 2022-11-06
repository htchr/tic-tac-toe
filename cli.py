# this file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.


from logic import make_empty_board, update_board, get_winner, other_player 


def print_board(board):
    count = 1
    moves = {}
    for i, r in enumerate(board):
        print('|', end='')
        for j, c in enumerate(r):
            if c == None:
                print(count, end='')
                moves[str(count)] = (i, j)
                count += 1
            else:
                print(c, end='')
            print('|', end='')
        print('')
    return moves


def enter_move(board, player, moves):
    print(f"{player}'s turn")
    turn = True
    while turn:
        move = input("choose next move: ")
        if move in list(moves.keys()):
            board = update_board(player, board, moves[move])
            turn = False
        else:
            print("please enter a valid move")
    return board


if __name__ == '__main__':
    board = make_empty_board()
    player = "X"
    winner = None
    while winner == None:
        moves = print_board(board)
        board = enter_move(board, player, moves)
        winner = get_winner(board)
        player = other_player(player)
    print(f"{winner} won!")
    print_board(board)
