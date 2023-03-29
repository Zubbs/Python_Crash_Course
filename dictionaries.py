# girlfriend = {}
# girlfriend['name'] = 'Florence'

# print(girlfriend)

# print(girlfriend['name'])

girlfriend = {'name':'Florence', 'age':'23', 'city':'Dublin'}
boyfriend = {'name':'Zubby', 'age':'25', 'city':'Dublin'}
friend = {'name':'Hassan', 'age':'26', 'city':'Paris'}

people = [girlfriend,boyfriend,friend]

for peep in people:
    print(peep)



# favourite_numbers = {'me': 4, 'her': 5, 'ss': 4}

# print(favourite_numbers['ss'])


# when looping through a dictionary, it is default behaviour to loop through the dictionary's .key()
# sorted() - sorting function, alphabetical
# a set() is similar to a list but every item must b

# rivers = {'nile': 'egypt', 'liffey': 'dublin', 'niger': 'nigeria'}

# for river,place in rivers.items():
#     print(f'The {river.title()} runs through {place.title()}')


# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# for name, language in favourite_languages.items():
#     print(name.title() + "'s favourite language is "
#      +
#         language.title() + ".")


# take_poll = ['jen', 'Edward', 'Zubby', 'frank']

# for people in take_poll:
#     if people.lower() in favourite_languages.keys():
#         print(f'Thank you for responding, {people.title()}')
#     else:
#         print(f'Please take the poll {people.title()}!')

number = input('tell me a number, lets see if it is a multiple of 10: ')

if int(number) % 10 == 0:
    print('it is')
else:
    print('Wrong')