car = 'Audi'
car.lower() == 'audi'


# python does not require an else block at the end of an if-elif chain. sometimes use elif to specify the exact conditional you want.
# multiple if statements do not rely on each any of them have passed the test before.
# in an if-elif-else chain, one one condition passes, python skips the rest



alien_color = 'red'

if alien_color == 'green':
    print('You just won 5 points')

elif alien_color == 'yellow':
    print('You just won 10 points')

elif alien_color == 'red':
    print('You just won 15 points')


age = 22

if age < 2:
    print('You are a baby')

elif age < 4:
    print('You are a toddler')

elif age < 13:
    print('You are a kid')

elif age < 20:
    print('You are a teenager')

elif age < 65:
    print('You are an adult')

elif age >= 65:
    print('you are an elder')



current_users = ['style', 'phoenix', 'admin', 'nzube', 'today']

new_users = ['style', 'phoenix', 'shoulder', 'youngjun', 'people', 'NZUBE']

if new_users:
    for new_user in new_users:
        if new_user.lower() in current_users:
            print('That username is taken, choose another')
        else:
            print('That username is available')

# if usernames:
#     for username in usernames:
#         if username == 'admin':
#             print(f'Hello {username.title()}, would you like to see a staus report?')
#         else:
#             print(f'Hello {username.title()}, thank you for logging in again')
# else:
#     print('We need to find more users')


ordinal_numbers = [1,2,3,4,5,6,7,8,9]

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print (f'{ordinal_number}st')
    elif ordinal_number == 2:
        print(f'{ordinal_number}nd')
    elif ordinal_number == 3:
        print(f'{ordinal_number}rd')
    elif ordinal_number >3:
        print(f'{ordinal_number}th')   
