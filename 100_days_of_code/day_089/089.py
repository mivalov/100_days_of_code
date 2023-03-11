# Day 89: Community chat application
from datetime import datetime

from flask import Flask, request, redirect
from replit import db

app = Flask(__name__, static_folder='static', template_folder='templates')


def open_page(file: str) -> str:
    with open(file, 'r') as stream:
        page = stream.read()
    return page


def get_chat(is_admin: bool = False) -> str:
    page = open_page('templates/message.html')
    keys = db.keys()
    keys = reversed(list(keys))
    messages = ''
    counter = 0
    for key in keys:
        if counter == 5:
            break
        msg = page
        msg = msg.replace('{username}', db.get(key, {}).get('username'))
        msg = msg.replace('{timestamp}', key)
        msg = msg.replace('{message}', db.get(key, {}).get('message'))
        if is_admin:
            delete_href = f'<a href="/delete?id={key}">X</a>'
            msg = msg.replace('{admin}', delete_href)
        else:
            msg = msg.replace('{admin}', '')
        messages += msg
        counter += 1
    return messages


@app.route('/')
def index():
    page = open_page('templates/index.html')
    page = page.replace(
        '{user}',
        request.headers.get('X-Replit-User-Name')
    )
    is_admin = request.headers.get('X-Replit-User-Name') == 'mvalov'
    page = page.replace('{content}', get_chat(is_admin))
    return page


@app.route('/add', methods=['POST'])
def add():
    form = request.form
    message = form.get('message')
    timestamp = str(int(datetime.now().timestamp()))
    # user_id = request.headers.get('X-Replit-User-Id')
    username = request.headers.get('X-Replit-User-Name')
    db[timestamp] = {
        # 'user_id': user_id,
        'username': username,
        'message': message,
    }
    return redirect('/')


@app.route('/delete', methods=['GET'])
def delete_msg():
    if request.headers.get('X-Replit-User-Name') != 'mvalov':
        return redirect('/')
    else:
        msg_key = request.values.get('id')
        # delete from db
        # del db[results]
        db.pop(msg_key)
        return redirect('/')


app.run(host='0.0.0.0', port=5000)
