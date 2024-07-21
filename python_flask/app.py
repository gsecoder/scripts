from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
