import json
from flask import Flask
app = Flask(__name__)

data = {
    'name' : 'plusoneeeee''',
    'height' : 155,
    'weight' : 40
}

jsonStr = json.dumps(data, sort_keys=True, indent=1)

@app.route("/")
def hello():
    return work(2)
def work(ins):
    return ins*ins

@app.route("/go", methods=['POST'])
def go():
    return jsonStr


@app.route('/testrtt')
def text():
    return '<html><body><h1>Hello World</h1></body></html>'
