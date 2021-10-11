import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0:
        print("Did you mean %s instead" %get_close_matches(word,data.keys())[0])
        decide=input("press y for yes or n for no")
        if decide=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide=="n":
            print("Please enter different word")
        else:
            print("please enter again, you have done something wrong")
    else:
        print("Please enter different word ! ")



word=input("Enter the word you want to search -> ")
word=word.lower()
output=translate(word)
if output:
    for x in output:
        print(x)
