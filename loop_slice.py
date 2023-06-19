# slicing basically has the same instructions as range() -> where loop[1:4] wil take all the elements from the first to the element before the third element.
# e.g for ['range', today', 'yesterday'], if we applied a loop of [-2:] it will print out - ['today', 'yesterday']

# [:] will include both the first and last elements so it is basically a copy


Pizzas = ['margarita', 'peperoni', 'haiwan', 'suya']

pizzas = Pizzas[1:]



print(pizzas)

friend_pizzas =  Pizzas[:]

# Pizzas.append('spanish')

# friend_pizzas.append('jamaican')

# print('My favorite Pizzas are:' + '\n')
# for x in Pizzas:
#     print(x)

print('My Friends favorite pizzas are: /n') 
for y in friend_pizzas:
    print(y)

# print('The first three items in ths list are: ')
# sliced = Pizzas[:3]
# print(sliced)

# print('three items from the middle of the list are: ')
# sliced = Pizzas[1:4]
# print(sliced)

print('the last three items in the list are: ')
sliced = Pizzas[1:4]
print(sliced)