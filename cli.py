import typing
from logic import TicTacToe, Human, Bot

def user_input(prompt: str, expected_answer: list, error_message: str) -> str:
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

def human_move(ttt: TicTacToe) -> None:
    """
    ask where the player wants to play, update board
    ttt: TicTacToe instance
    player: string 'X' or 'O'
    returns: None
    """
    moves = ttt.open_moves()
    print(f"it is {ttt.get_player()}'s turn")
    move = user_input(f'please choose an open position to play {moves}: ',
                      moves,
                      'please choose a valid open position to play')
    ttt.get_player().move(ttt, int(move))

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
            ttt.set_player_type('X', True)
            ttt.set_player_type('O', False)
        else:
            ttt.set_player_type('X', False)
            ttt.set_player_type('O', True)
    else:
        ttt.set_player_type('X', True)
        ttt.set_player_type('O', True)
    # play game
    while ttt.get_winner() == None:
        print(ttt, end='\n\n')
        if isinstance(ttt.get_player(), Human):
            human_move(ttt)
        else:
            ttt.get_player().move(ttt)
        ttt.check_winner()
        ttt.switch_player()
    print(ttt, end='\n\n')
    print(ttt.get_winner())

