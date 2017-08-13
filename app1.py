import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(s_word):
  s_word = s_word.lower()
  if s_word in data:
    return data[s_word]
  elif len(get_close_matches(s_word, data.keys())) > 0:
    yn = input("Did you mean %s instead? Enter Y/N: " %get_close_matches(s_word, data.keys())[0])
    if yn == "Y":
      return data[get_close_matches(s_word, data.keys())[0]]
    elif yn == "N":
      return "The word does not exist. Please check it again."
    else:
      return "Please do it again."
  else:
    return "The word does not exist. Please check it again."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
  for item in output:
    print(item)
else:
  print(output)
