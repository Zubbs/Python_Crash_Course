import json
# The json module allows you to dump simple Python data structures into a file and load the data from the file, the next time the program runs.

# You can also use jsons to share data between different programs irrespective of programming language

# Refactoring is when you break down your code into a series of functions that have specific jobs


numbers = [2,3,4,5,7]

filename = 'numbers.json'

with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)    # source -> destination

with open(filename) as f_obj:
    content = json.load(f_obj)
    print(content)