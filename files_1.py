with open('learning_python.txt') as file_object:
    content = file_object.read()
    print(content.strip())


with open('learning_python.txt') as file_object:
    for x in file_object:
        y = x.replace('Python','C')
        print(y.strip())


with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    y = line.replace('Python','C')
    print(y.rstrip())
    

# print(outside)

# for x in outside:
#     print(x)