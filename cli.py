import typing
from logic import Player, TicTacToe, Bot

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

class Human(Player):
    def move(self, ttt: TicTacToe) -> None:
        """ask user for open move and update ttt board"""
        moves = ttt.open_moves()
        print(f"it is {ttt.get_player()}'s turn")
        move = user_input(f'please choose an open position to play {moves}, (enter 0 to quit): ',
                          moves + ['0'],
                          'please choose a valid open position to play')
        if move == '0':
            ttt.get_db().save()
            quit()
        else:
            ttt.update_board(move)

if __name__ == "__main__":
    # game set up
    ttt = TicTacToe()
    n_players = user_input('how many humans are playing today? (0, 1, 2): ',
                           ['0', '1', '2'],
                           'please choose a number between 0 and 2')
    if n_players == '0':
        ttt.set_player_type('X', Bot('X'))
        ttt.set_player_type('O', Bot('O'))
    elif n_players == '1':
        xo = user_input('would you like to play X or O? X goes first: ',
                        ['X', 'O'],
                        'please enter X or O, capitalization matters')
        if xo == 'X':
            ttt.set_player_type('X', Human('X'))
            ttt.set_player_type('O', Bot('O'))
        else:
            ttt.set_player_type('X', Bot('X'))
            ttt.set_player_type('O', Human('O'))
    else:
        ttt.set_player_type('X', Human('X'))
        ttt.set_player_type('O', Human('O'))
    # play game
    while ttt.get_winner() == None:
        print(ttt, end='\n\n')
        ttt.get_player().move(ttt)
        ttt.check_winner()
        ttt.switch_player()
    print(ttt, end='\n\n')
    print(ttt.get_winner(), end='\n\n')
    print(ttt.post_game_stats())

