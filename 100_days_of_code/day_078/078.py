# Day 78: Reflections

from flask import Flask

app = Flask(__name__, template_folder='templates')

my_reflections = {
    '39': {
        'link': 'https://replit.com/@mvalov/Day-39-Hangman',
        'reflection': 'Reflection for day 39',
    },
    '59': {
        'link': 'https://replit.com/@mvalov/Day59100Days',
        'reflection': 'Reflection for day 59',
    },
}


@app.route('/')
def index():
    page = f"""<html><body>
    <h1>Hello from Flask!</h1>
    <p><a href='/39'>Challenge 39</a></p>
    <p><a href='/59'>Challenge 59</a></p>
    </body></html>"""
    return page


@app.route('/<page_number>')
def page(page_number):
    refs = my_reflections.get(page_number, {})
    with open('templates/reflections.html', 'r') as file:
        page = file.read()
    page = page.replace('{day}', page_number)
    page = page.replace('{link}', refs.get('link'))
    page = page.replace('{reflection}', refs.get('reflection'))
    return page


app.run(host='0.0.0.0', port=5000)
