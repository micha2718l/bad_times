import random

from flask import Flask


app = Flask(__name__)

with open('negative_words.txt') as f:
    neg_words = f.readlines()
    neg_words = [n.strip() for n in neg_words]

with open('animals.txt') as f:
    animals = f.readlines()
    animals = [a.strip() for a in animals]

def bad_time():
    return random.choice(neg_words) + ' ' + random.choice(animals)

@app.route('/')
def hello_world():
    return f'''<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <title>Some new random bad time.</title>

</head>

<body>

  <h1>Your new bad time is.....</h1>
  <p>{bad_time()}</p>

</body>

</html>'''

if __name__ == '__main__':
    app.run()