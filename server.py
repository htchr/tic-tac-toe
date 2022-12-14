from flask import Flask, render_template, request, redirect
from logic import Player, TicTacToe, Bot

app = Flask(__name__)
ttt = TicTacToe()

class Human(Player):
    def move(self, ttt):
        return redirect('/play')

@app.route('/play', methods=['POST', 'GET'])
def play(ttt=ttt):
    if request.method == 'GET':
        return render_template('play.html', ttt=ttt)
    move = request.form['move']
    if move not in ttt.open_moves():
        return render_template('play.html', ttt=ttt)
    ttt.update_board(move)
    ttt.switch_player()
    return redirect('/controlflow')

@app.route('/stats')
def stats(ttt=ttt):
    return render_template('stats.html', ttt=ttt)

@app.route('/controlflow')
def controlflow(ttt=ttt):
    ttt.check_winner()
    if ttt.get_winner() != None:
        return redirect('/stats')
    if isinstance(ttt.get_player(), Human):
        return ttt.get_player().move(ttt)
    ttt.get_player().move(ttt)
    ttt.switch_player()
    return redirect('/controlflow')

@app.route('/', methods=['POST', 'GET'])
def index(ttt=ttt):
    if request.method == 'GET':
        return render_template('index.html')
    n_humans = int(request.form['n_humans'])
    if n_humans == 0:
        ttt.set_player_type('X', Bot('X'))
        ttt.set_player_type('O', Bot('O'))
    elif n_humans == 1:
        ttt.set_player_type('X', Human('X'))
        ttt.set_player_type('O', Bot('O'))
    elif n_humans == 2:
        ttt.set_player_type('X', Human('X'))
        ttt.set_player_type('O', Human('O'))
    else:
        return render_template('index.html')
    return redirect('/controlflow')

if __name__ == '__main__':
    app.run(debug=True)

