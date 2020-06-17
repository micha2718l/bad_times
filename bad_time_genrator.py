import random

import Flask from flask


app = Flask(__name__)

with open('negative_words.txt') as f:
    neg_words = f.readlines()
    neg_words = [n.strip() for n in neg_words]

with open('animals.txt') as f:
    animals = f.readlines()
    animals = [a.strip() for a in animals]

def bad_time():
    return random.choice(neg_words) + ' ' + random.choice(animals))

@app.route('/')
def hello_world():
    return bad_time()