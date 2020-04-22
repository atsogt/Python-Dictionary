import json

from difflib import get_close_matches

data = json.load(open('data.json'))

word = input('Enter Word: ')


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input('Is this the word you meant %s? If yes press Y or if no press N: ' % get_close_matches(
            w, data.keys())[0])
        if yn == 'y':
            return data[get_close_matches(w, data.keys())[2]]
        elif yn == 'n':
            return 'word is not matching.'
    else:
        return "Word not found"


print(translate(word))
