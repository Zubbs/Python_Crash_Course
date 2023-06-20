# value = 0
# sum = True
# while sum == True:

#     number = input('Type a number you would like to add up: ')
#     if number == 'stop':
#         sum = False
#     try:
#         value += int(number)
#     except ValueError:
#         print(f'The input you typed {number} is not a digit')
#     else:
#         print(value)


def open_file(filename):
    try:
        with open(filename) as file_object:
            content =  file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(content)


filenames = ['dogs.txt', 'monkey.txt' , 'cats.txt']

for filename in filenames:
    open_file(filename)
