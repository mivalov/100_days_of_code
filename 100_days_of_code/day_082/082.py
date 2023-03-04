# Day 82: GET Method

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello there!'


@app.route('/language', methods=['GET'])
def language():
    data = request.args
    if not data:
        return 'No arguments given'
    lang = data.get('lang').lower()
    if lang == 'en':
        return 'Hello, welcome to the page in English!'
    elif lang == 'de':
        return 'Hallo, willkommen auf der Seite auf Deutsch!'
    elif lang == 'bg':
        return 'Здравейте, добре дошли в страницата на български!'
    elif lang == 'fr':
        return 'Bonjour, bienvenue sur la page en français!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
