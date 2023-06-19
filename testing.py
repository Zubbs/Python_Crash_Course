
def show_magicians(names):
    for name in names:
        print (name.title())


def make_great(names):
    new_names = []
    while names:
        old_name = names.pop()
        new_name = 'The Great ' + old_name
        new_names.append(new_name)

    for new_name in new_names:
        names.append(new_name)

    
    return names

          
    

   

names = ['houdini', 'flacko', 'tombrown']

# show_magicians(names) 

names_changed = make_great(names[::-1])#[:])  # pop takes this in reverse to print the list in the correct order
print(names)
print(names_changed)
show_magicians(names)
