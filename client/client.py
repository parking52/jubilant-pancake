from flask import Flask, request
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/register')
def register():
    return 'Hello, World!'


@app.route('/play')
def play():
    return 'Hello, World! {value}'.format(value=app.config['CLIENT'].value)


class Client(object):

    def __init__(self):
        self.value = 123


class Game(object):

    def __init__(self, game_nummer):
        self.game_nummer = game_nummer


@app.route('/game/<game_nummer>')
def game(game_nummer):

    new_game = Game(game_nummer)

    return 'Hello, World! :-)' + str(new_game.game_nummer)


@app.route('/game_endpoint/<game_nummer>', methods=['POST'])
def game_called(game_nummer):

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"


def create_app(client):

    app.config['CLIENT'] = client
    return app


if __name__ == '__main__':

    client = Client()
    app = create_app(client)
    app.run(debug=True, host='0.0.0.0')

