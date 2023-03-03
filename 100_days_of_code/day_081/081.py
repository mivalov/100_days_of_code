# Day 81: I am not a Robot

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    with open('form.html', 'r') as stream:
        page = stream.read()
    return page


@app.route('/robot', methods=['POST'])
def robot():
    robot_msg = 'You are a robot!'
    form = request.form
    if form.get('metal') == 'yes':
        return robot_msg
    elif form.get('infinity') and 'error' in form.get('infinity').lower():
        return robot_msg
    elif form.get('food') == 'synthetic oil':
        return robot_msg
    else:
        return 'Hi there fellow human'


app.run(host='0.0.0.0', port=5000)
