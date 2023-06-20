# Username = input('Please type in what your name is: ')

# with open('guest.txt', 'w') as file_object:
#     file_object.write(Username)


username = ''
while username not in ['q','Q']:
    username = input('Please type in what your name is: ')
    if username in ['q', 'Q']:
        break
    print(f'Good morning {username}')
    with open('guest_book.txt', 'a') as write_object:
        write_object.write(username + '\n')