for number in range(1,21):
    print(number)

million = [x for x in range(1,1000001)]
#for numbers in million:
#    print(numbers)
# print(sum(million))


odd_numbers_list = [x for x in range(1,21,2)]

multiples_of_threes = list(range(3,33,3))
print(multiples_of_threes)
# for number in multiples_of_threes:
# #    print(number)



cubes = [x**3 for x in range(1,11)]
for cube in cubes:
    print(cube)
