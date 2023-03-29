Pizzas = ['margarita', 'peperoni', 'haiwan', 'suya']


for pizza in Pizzas:
    print('I like ' + pizza.title() + ' pizza')

print('I really love pizza!')


Animals =  ['dog', 'cat', 'bird']

for animal in Animals:
    print('a ' + animal.title() + ' would make a good pet')

print('any of these animals will make a great pet')


#Range(1,5) counts from the first and omits the last value

# for x in range(0,4):# print all the values between 1 and (1,5)
#     print(Pizzas[x])

#list Comprehension 
# typical scenario is:
squares = [] 
for x in range(1,11):
   squares.append(x**2)

print(squares)


squares_ = [x**2 for x in range(1,11)]

print(squares_)
