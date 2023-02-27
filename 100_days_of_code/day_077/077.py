from flask import Flask, redirect
import datetime

app = Flask(__name__, static_folder='static', template_folder='templates')


def update_page(title: str, text: str) -> str:
    today = datetime.date.today().strftime("%B %d")
    f = open('templates/blog.html', 'r')
    page = f.read()
    f.close()
    page = page.replace('{title}', title)
    page = page.replace('{date}', today)
    page = page.replace('{text}', text)
    return page


@app.route('/')
def index():
    return 'Hello World'


@app.route('/blog/39')
def redirect_blog_post1():
    return redirect('/39')


@app.route('/blog/hello_world')
def redirect_hello_world():
    return redirect('/hello_world')


@app.route('/39')
def blog_post1():
    title = 'Day 39 Solution'
    text = 'The challenge for day 39 was to build a game called "Hangman". ' \
           'It was a tricky project, mostly because of the game logic. ' \
           'I added an extra feature to print out the remaining lives in ' \
           'addition to the ascii representation of the game being ' \
           'displayed in the console.'
    return update_page(title, text)


@app.route('/hello_world')
def hello_world():
    title = 'Hello World'
    text = 'Here is my first blog entry.'
    return update_page(title, text)


app.run(host='0.0.0.0', port=5000)
