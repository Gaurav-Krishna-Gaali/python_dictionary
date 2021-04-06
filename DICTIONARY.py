
import json
# library to get the close matches between wronly entered words
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]
    
    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input(" Press y for yes and n for no ? ---------->  ")
        if decide == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        
        elif decide == 'n':
            return('The word do not exit MIKE!!')

        else :
            return("You have entered wrong input. just enter y or n")



    else:
        print("You've entered the wrong word MIKE!!. please try again......!!!!")

word=input("Enter the word you the meaning for? ------------>>>   ")
Output = translate(word)

if type(Output) == list:
    for item in Output:
        print(item)

else:
    print(Output)



