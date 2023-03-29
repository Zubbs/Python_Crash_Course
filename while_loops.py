# break() will exit out of a while loop and won't run any code following that loop. Break works in for loops too
# continue goes back to the start of the loop. consider the program below used to print odd numbers


number = 0

while number < 10:
    number += 1

    if number % 2 == 0:
        continue

    else:
        print(number)


pizza_toppings = 'Keep saying what you Want'
pizza_toppings += '\nType quit to stop: '
active = True
prompt = ''

while prompt != 'quit':

    prompt = input(pizza_toppings)

    # if prompt == 'quit':
    #     active = False

    if prompt != 'quit':
        print(f'I will add {prompt}')





sandwich_orders = ['chicken', 'tuna','club', 'beef', 'prawn', 'pastrami', 'pastrami', 'pastrami']

finished_orders = []

print('Unfortunately we have run out of pastrami')

while 'pastrami' in sandwich_orders:

    sandwich_orders.remove('pastrami')


while sandwich_orders:

    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich')
    finished_orders.append(sandwich)


print(sandwich_orders)

for sandwich in finished_orders:
    print(sandwich.title())









vacation = {}

asking = True


while asking:
    name = input('what is your name? ')
    destination = input('\n What is your dream destination? ')

    vacation[name] = destination

    repeat = input('should i ask again? yes/no: ')
    if repeat == 'no':
        asking = False
    
    else:
        continue


for name, destination in vacation.items():
    print(f'{name} dream destination is {destination}')