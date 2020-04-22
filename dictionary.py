import json
import difflib
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(w):
    w = w.lower()
    if word in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input('Did you mean %s instead? Press Y for yes or press N for no: ' %
                   get_close_matches(w, data.keys())[0])
        if yn == 'Y' or yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N' or yn == 'n':
            return "Your word doesn't match."
        else:
            return "Your query doesn't exist."
    else:
        return 'Please double check your word.'


word = input('enter word: ')

output = translate(word)


if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
