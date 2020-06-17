import random

with open('negative_words.txt') as f:
    neg_words = f.readlines()
    neg_words = [n.strip() for n in neg_words]

with open('animals.txt') as f:
    animals = f.readlines()
    animals = [a.strip() for a in animals]

print(random.choice(neg_words) + ' ' + random.choice(animals))