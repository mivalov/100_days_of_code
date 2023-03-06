# Day 84: Client Server Logins

from flask import Flask, request, redirect
from replit import db

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    with open('templates/index.html', 'r') as stream:
        page = stream.read()
    return page


@app.route('/signup')
def signup():
    with open('templates/signup.html', 'r') as stream:
        page = stream.read()
    return page


@app.route('/signup', methods=['POST'])
def create_user():
    form = request.form
    keys = db.keys()
    username = form.get('username', '')
    if username not in keys:
        db[username] = {
            'name': form.get('name'),
            'password': form.get('password'),
        }
        return redirect('/login')
    else:
        return redirect('/signup')


@app.route('/login')
def login():
    with open('templates/login.html', 'r') as stream:
        page = stream.read()
    return page


@app.route('/login', methods=['POST'])
def log_in():
    form = request.form
    keys = db.keys()
    username = form.get('username')
    if username not in keys:
        return redirect('/login')
    else:
        if form.get('password') == db.get(username, {}).get('password'):
            return f'<h1>Hello {username}</h1>'
        else:
            return redirect('/login')


app.run(host='0.0.0.0', port=5000)
