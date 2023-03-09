# Day 87: Blog + Authentication
import os

from flask import Flask, redirect, session, request
from replit import db

app = Flask(__name__, template_folder='templates', static_folder='static')

# db['user'] = {'username': 'david', 'password': 'baldy1'}

# secret key should be stored as secret in replit and sth like '0wd8!3$[%FWer2'
app.secret_key = os.getenv('SECRET_KEY')


def get_blog_posts():
    with open('templates/blog_post.html', 'r') as stream:
        blog_post = stream.read()
    keys = db.keys()
    # simple descending date order
    keys = reversed(list(keys))
    blog_posts = ''
    for key in keys:
        current_blog_post = blog_post
        if key != 'user':
            current_blog_post = current_blog_post.replace(
                '{title}',
                db.get(key).get('title')
            )
            current_blog_post = current_blog_post.replace(
                '{date}',
                db.get(key).get('date')
            )
            current_blog_post = current_blog_post.replace(
                '{text}',
                db.get(key).get('text')
            )
            blog_posts += current_blog_post
    return blog_posts


@app.route('/')
def index():
    user_id = request.headers.get('X-Replit-User-Name')
    if user_id == 'mvalov':
        return redirect('/welcome')
    with open('templates/blog.html', 'r') as stream:
        page = stream.read()
    page = page.replace('{content}', get_blog_posts())
    return page


@app.route('/login')
def login():
    user_id = request.headers.get('X-Replit-User-Name')
    if user_id != 'mvalov':
        return redirect('/welcome')
    with open('templates/login.html', 'r') as stream:
        page = stream.read()
    page = page.replace('{content}', get_blog_posts())
    return page


@app.route('/login', methods=['POST'])
def log_in():
    user_id = request.headers.get('X-Replit-User-Name')
    if user_id != 'mvalov':
        return redirect('/welcome')
    form = request.form
    user = db.get('user', {})
    if form.get('username') == user.get('username') \
            and form.get('password') == user.get('password'):
        session['user_accepted'] = True
        return redirect('/welcome')
    else:
        return redirect('/login')


@app.route('/welcome')
def welcome():
    user_id = request.headers.get('X-Replit-User-Name')
    if user_id != 'mvalov':
        return redirect('/')
    with open('templates/welcome.html', 'r') as stream:
        page = stream.read()
    page = page.replace('{content}', get_blog_posts())
    return page


@app.route('/add', methods=['POST'])
def add():
    form = request.form
    blog_post = {
        'title': form.get('title'),
        'date': form.get('date'),
        'text': form.get('text'),
    }
    db[form.get('date')] = blog_post
    return redirect('/welcome')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(host='0.0.0.0', port=5000)
