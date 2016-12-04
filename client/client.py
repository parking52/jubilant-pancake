from flask import Flask
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


def create_app(client):

    app.config['CLIENT'] = client
    return app


if __name__ == '__main__':

    client = Client()
    app = create_app(client)
    app.run(debug=True, host='0.0.0.0')

