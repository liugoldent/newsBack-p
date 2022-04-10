import json
from flask import Flask, request
from flask_cors import CORS
from pkg_resources import require
app = Flask(__name__)
CORS(app, resources={r"/.*": {"origins": ["http://localhost:3000","https://news-frontend-g.herokuapp.com/"]}})


data = {
    'name' : 'plusoneeeee''',
    'height' : 155,
    'weight' : 40
}

jsonStr = json.dumps(data, sort_keys=True, indent=1)

@app.route("/")
def h():
    name = hello()
    demo = abc()
    return "Hi {name}, you are {demo}".format(name=name, demo=demo)
def hello():
    return 'Hello'
def abc():
    return 'Woeld'


@app.route("/word", methods=['POST'])
def go():
    print(request.json)
    return "JSON"+request.json.get('firstName')

@app.route('/testrtt')
def text():
    return '<html><body><h1>Hello World</h1></body></html>'
