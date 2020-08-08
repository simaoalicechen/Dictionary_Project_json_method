import json 
from difflib import get_close_matches

data = json.load(open("data.json", 'r')) 

def translator(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: 
        return data[w.title()]  
    elif w.upper() in data: 
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        question = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        question = question.upper()
        if question == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif question == "N":
          while len(get_close_matches(w, data.keys()))>1:
            try:
              question2 = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w, data.keys())[1])
              question2 = question2.upper()
              if question2 =="Y": 
                return data[get_close_matches(w, data.keys())[1]]
              else: 
                return f"Sorry, we can't find the word '{word}' you are looking for. Please try again."
              break
            except ValueError:
              print("We didn't understand your entry. Please try again.")
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")
output = translator(word)

if type(output) == list: 
  for item in output: 
    print(item)
else: 
  print(output)


