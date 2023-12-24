from flask import Flask

app = Flask(__name__)


def hello_world():
    return 'Hello, World!'


app.add_url_rule('/', view_func=hello_world, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
