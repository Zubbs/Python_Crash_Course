
def show_magicians(names):
    for name in names:
        print (name.title())

def new_name(names):
    newname = 'The Great '
    for x in names:
        names.append(newname+x)

# def make_great(names):
#     new_names = []
#     while names:
#         old_name = names.pop()
#         new_name = 'The Great ' + old_name
#         new_names.append(new_name)

#     for new_name in new_names:
#         names.append(new_name)

    
#     return names

          
    

   

names = ['houdini', 'flacko', 'tombrown']

show_magicians(names)

new_name(names)

names_changed = make_great(names[:][::-1])  # pop takes this in reverse, using this i reversed the copied list before popping it
print(names_changed)
show_magicians(names)