import json

def get_stored_username():
    """Get Stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return False
    else:
        return username
    
def get_new_username():
    """Prompt for new username"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    """Greet the user by name. """
    try:
        username = get_stored_username()


    except:
        pass

    else:
        print(f'is that you {username}: ')
        correct = input(f'is that you {username}: ')
        correct = correct.lower()
        if correct in ['yes', 'y']:
            print(f'Welcome back, {username}! ')
        else:
            username = get_new_username()
            print(f'we will remember when you come back {username}')
 


greet_user()