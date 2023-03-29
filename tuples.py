# tuples are immutable lists. Their value does not change. They look like list definitions just that you use parantheses instead of a square. 

# example havng a rectangle that its dimensions does not change. 

dimensions = (200, 45)

print(dimensions[0])


buffet_resturant =  ('beans', 'rice', 'salad', 'soup', 'steak')

for food in buffet_resturant:
    print(food)

# buffet_resturant[1] = 'stew'

buffet_resturant = ('beans', 'rice', 'salad', 'soup', 'steak', 'garri')


for food in buffet_resturant:
    print(food)