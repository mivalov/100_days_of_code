# Day 85: Extend the Login system from day 84
import os

from flask import Flask, request, redirect, session
from replit import db

app = Flask(__name__, template_folder='templates')
# add a secret to replit -> something like 'fUne2f?4[)§%/&'
app.secret_key = os.getenv('sessionKey')


@app.route('/')
def index():
    if session.get('logged_in'):
        return redirect('/welcome')
    with open('templates/index.html', 'r') as stream:
        page = stream.read()
    return page


@app.route('/signup')
def signup():
    if session.get('logged_in'):
        return redirect('/welcome')
    with open('templates/signup.html', 'r') as stream:
        page = stream.read()
    return page


@app.route('/signup', methods=['POST'])
def create_user():
    if session.get('logged_in'):
        return redirect('/welcome')
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
    if session.get('logged_in'):
        return redirect('/welcome')
    with open('templates/login.html', 'r') as stream:
        page = stream.read()
    return page


@app.route('/login', methods=['POST'])
def log_in():
    if session.get('logged_in'):
        return redirect('/welcome')
    form = request.form
    keys = db.keys()
    username = form.get('username')
    if username not in keys:
        return redirect('/login')
    else:
        if form.get('password') == db.get(username, {}).get('password'):
            # successful login
            session['logged_in'] = username
            return redirect('/welcome')
        else:
            return redirect('/login')


@app.route('/welcome')
def welcome():
    with open('templates/welcome.html', 'r') as stream:
        page = stream.read()
        page = page.replace(
            '{username}',
            db.get(session.get('logged_in')).get('name')
        )
    return page


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(host='0.0.0.0', port=5000)
