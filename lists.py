names = ['Obinna', 'Nzube', 'Thomas']

print(names)

for name in range(len(names)):
    print(names[name])



# .insert(0, 'new_string) is a method for appending at unique position .pop() removes last element in list
# .pop can also remove items in a unique position in a list 

# so many ways to delete, del lists[1], will delete the item without storing the value
# list.pop(0) can store that removed unique item in that method
# remove ('free') will delete the item based on value

#NOTE remove() only gets rid of the first occurence of the value you specify


Guest_list = ['Obinna', 'Nzube', 'Thomas']

print(Guest_list[0].title() + ", you're invited to dinner!")
print(Guest_list[1].title() + ", you're invited to dinner!")
print(Guest_list[2].title() + ", you're invited to dinner!")

Cant_make_it = Guest_list.pop(2)
print(Cant_make_it + " won't be joining us")
print(Guest_list)

print ("Found a bigger table so inviting more people")

Guest_list.insert(0,'Tola')
Guest_list.insert(2,'David')
Guest_list.append('Fola')
print(Guest_list)

gone = Guest_list.pop()
print(gone + ' cannot make it') 
print(gone  + ' cannot make it') 

print(Guest_list)


#using .sort()
# for reverse alphabetical order is (reverse=True)
#sorted function sorts the value of the list but does not affect the original
# .sort() sorts the value of the list in place. You would have to print an original to see an output.
#.reverse() reverses the order of the list
Guest_list.reverse()

print(Guest_list) 

print(sorted(Guest_list))





