from random import randint
from logic import TicTacToe

def user_input(prompt, expected_answer, error_message):
    """
    deal with user input, repeat message and error message
    until user inputs one of the expected answers
    prompt: string for python input
    expected_answer: list of values to check for
    error_message: string to print when user inputs unexpected value
    returns: string of user input
    """
    while True:
        answer = input(prompt)
        if answer not in expected_answer:
            print(error_message)
        else:
            return answer

def human_move(ttt, player):
    """
    ask where the player wants to play, update board
    ttt: TicTacToe instance
    player: string 'X' or 'O'
    returns: None
    """
    moves = ttt.open_moves()
    move = user_input(f'please choose an open position to play {moves}: ',
                      moves,
                      'please choose a valid open position to play')
    ttt.update_board(player, int(move))

def bot_move(ttt, player):
    """
    generate random play from bot
    ttt: TicTacToe instance
    player: string 'X' or 'O'
    returns: None
    """
    moves = ttt.open_moves()
    while True:
        move = str(randint(1, 9))
        if move in moves:
            ttt.update_board(player, int(move))
            break

if __name__ == "__main__":
    ttt = TicTacToe()
    # player set-up
    n_players = user_input('how many humans are playing today? (0, 1, 2): ',
                           ['0', '1', '2'],
                           'please choose a number between 0 and 2')
    if n_players == '0':
        ttt.set_player_type('X', False)
        ttt.set_player_type('O', False)
    elif n_players == '1':
        xo = user_input('would you like to play X or O? X goes first: ',
                        ['X', 'O'],
                        'please enter X or O, capitalization matters')
        if xo == 'X':
            ttt.set_player_type('O', False)
        else:
            ttt.set_player_type('X', False)
    # play game
    player = 'X'
    while ttt.get_winner() == None:
        print(ttt, end='\n\n')
        if ttt.get_player_type(player):
            human_move(ttt, player)
        else:
            bot_move(ttt, player)
        ttt.check_winner()
        player = ttt.other_player(player)
    print(ttt, end='\n\n')
    print(ttt.get_winner())


