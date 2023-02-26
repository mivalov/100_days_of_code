# Day 76: Flask

from flask import Flask, url_for

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    page = f"""<html><body>
    <h1>Hello from Flask!</h1>
    <p><a href='/portfolio'>Portfolio</a></p>
    <p><a href='/linktree'>Linktree</a></p>
    </body></html>"""
    return page


@app.route('/portfolio')
def portfolio():
    page = f"""<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>My Portfolio</title>
  <link href="{url_for('static', filename='css/portfolio.css')}" rel="stylesheet" type="text/css" />
</head>

<body>
  <!-- https://day73100days.mvalov.repl.co/ -->
  <h1>Miroslav's Portfolio</h1>
  <h2>Day 39 Solution</h2>
  <p>The challenge for day 39 was to build a game called "Hangman". It was a tricky project, mostly because of the game logic. I added an extra feature to print out the remaining lives in addition to the ascii representation of the game being displayed in the console. </p>
  <a href="https://replit.com/@mvalov/Day-39-Hangman"><img src="static/images/39.png"></a>
  <script src="script.js"></script>

 <!--
  This script places a badge on your repl's full-browser view back to your repl's cover
  page. Try various colors for the theme: dark, light, red, orange, yellow, lime, green,
  teal, blue, blurple, magenta, pink!
  -->
  <script src="https://replit.com/public/js/replit-badge.js" theme="blue" defer></script>
</body>

</html>"""
    return page


@app.route('/linktree')
def linktree():
    page = f"""<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="{url_for('static', filename='css/linktree.css')}" rel="stylesheet" type="text/css"/>
</head>

<body>
<img src="static/images/image.png" alt="Image">
<h1>Miroslav Valov</h1>
<p class="about">The infamous software developer you've ever met!</p>
<h2>Socials</h2>
<ul>
  <li><a href="https://github.com/mivalov">GitHub (mivalov)</a></li>
  <li><a href="https://replit.com/@mvalov">replit (@mvalov)</a></li>
</ul>
<script src="script.js"></script>

<!--
 This script places a badge on your repl's full-browser view back to your repl's cover
 page. Try various colors for the theme: dark, light, red, orange, yellow, lime, green,
 teal, blue, blurple, magenta, pink!
 -->
<script src="https://replit.com/public/js/replit-badge.js" theme="blue"
        defer></script>
</body>

</html>"""
    return page


app.run(host='0.0.0.0', port=5000)
