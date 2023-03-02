# Day 80: Longin Form + Flask

from flask import Flask, request

app = Flask(__name__)

data = {
    'paul': {
        'email': 'paul@gmail.com',
        'password': 'verySecret123'
    },
    'eva': {
        'email': 'eva@gmail.com',
        'password': 'ev197'
    },
    'andrew': {
        'email': 'andrew@gmail.com',
        'password': '%T&Afdq1V/'
    }
}


@app.route('/')
def index():
    page = """<!DOCTYPE html>
    <html>
    
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width">
      <title>replit</title>
      <link href="style.css" rel="stylesheet" type="text/css"/>
    </head>
    
    <body>
    <form action="/login" method="post">
      <p>Username: <input type="text" name="username" required></p>
      <p>Email: <input type="email" name="email" required></p>
      <p>Password: <input type="password" name="password" required></p>
      <button type="submit">Login</button>
    </form>
    </body>
    
    </html>"""
    return page


@app.route('/login', methods=['POST'])
def login():
    form = request.form
    try:
        details = data[form.get('username')]
    except IndexError:
        return 'Username, email or password is incorrect!'
    else:
        if form.get('email') == details.get('email') and form.get('password') == details.get('password'):
            return 'Login successful!'
        else:
            return 'Username, email or password is incorrect!'


app.run(host='0.0.0.0', port=5000)
