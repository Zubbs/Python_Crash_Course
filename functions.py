from argparse import _ArgumentGroup


# def display_message():
#     """This functions displays what I learnt"""
#     print("I leant about paramters being the piece of information you give to a function while arguments are the pieces of information you move from a function call to a function")





# def favourite_book(title):
#         print(f"One of my favourite food ` is {title}")


# favourite_book('snail')

#positional arguments are arguments you pass on relative to the position and Python tracks them with appropraite parameters defined in the function
#keyword arguments are arguments passed with name-value pairs, hence freeing you from following an order
#default values can be specified while defining a parameter. If an argument is defined in a function call, python uses that. else, it defaulsts to default value specified in the parameter
# when using default values it is good practice to list them after all that parameters that don't have any

# def make_shirt(size='Large',text='I love Python'):
#     print(f'The size of this shirt is {size} and the text written on it is {text}')

# make_shirt('15','Love')
# make_shirt(text='Peace', size='2')

# make_shirt()
# make_shirt(size='Medium', text='Peace only')


# def describe_city(name,country='Ireland'):
#     print(f'{name} is in {country}')
#     print(name + 'is in' + country)


# describe_city('London', country='UK')


# ----optional arguments can be valid where not all paramaters can be fufilled. You can define this by giving the optional paramter a default value of '' 


# def city_country():
#     name = input('Type the name of the city: ')
#     country = input('Type the country the city is located in: ')
#     answer = name.title() + ',' + ' ' + country.title()  
#     return answer

# city_country = city_country()
# print(city_country)
# print(type(city_country))


def make_album(num_tracks = ''):

    while True:
        print('Type in q at any point to quit')
        artist_name = input('Type in your name: ')
        userful_data = 'not enough info'
        
    
        if artist_name == 'q':

            break
            
        album_title = input('Type in album name: ')
        if album_title == 'q':
            break

        if artist_name and album_title:
            userful_data = {'Name':artist_name.title(), 'Title':album_title.title()}
        
        if num_tracks:
            userful_data['num_tracks'] = num_tracks
            print(userful_data)

        else:
            userful_data = 'not enough info'
        
      
    

    return userful_data

new = make_album(num_tracks = 2)
print(new)


# sometimes when using functions you might want to keep your list intact i.e not allow the function to affect the list, in this case pass on a copy of the list to the function
# e.g def new_function(listed[:])


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

names_changed = make_great(names[:][::-1])  # pop takes this in reverse, using this i reversed the copied list before popping it
print(names_changed)
show_magicians(names)


# arbitrary number of arguments help when you don't know how many arguments you need to put in a function. So you define a parameter with an * - e.g like def new (*something)
# this parameter creates a tuple something that will hold all the arguments passed to it. Python packs the argument into a tuple even if it is just one element

def pizza(*toppings):
    print('\n We are making pizza with the following toppings: ')
    for topping in toppings:
        print(f'- {topping}')


pizza('margarita', 'haiwan')
    

# you can mix different types of parameters but rememeber to place the different ones apart from positional after



# also you can use these arbitrary arguments with key value pairs using ** in the paramters but these will create a dictionary for the arguments to pass key and value info too


def build_profile(first,last, **userinfo):  # **userinfo makes an arbitrary dictionary
    """Build a dictionary containing everything we know about a user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in userinfo.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')

print(user_profile)



def sandwiches(*items_wanted):
    print('\n We are preparing this sandwich with the following ingredients: ')

    for item in items_wanted:
        print(f'- {item}')


sandwiches('ham', 'chicken')


sandwiches('gizzard')

sandwiches('cheese', 'lemon')


def make_car(manufacturer_, model_, **other_info):
    car_type = {}
    car_type['manufacturer'] = manufacturer_
    car_type['model'] = model_

    for key,value in other_info.items():
        car_type[key] = value

    print(car_type)


make_car('subaru', 'outback', color = 'blue', tow_package = True)

### MODULES 
# you can sort your functions by storing them in a seperate file called a module. You can then import the module to your main program
# import pizza
# to call a function from an imported module, enter the name of the module you imported followed by a dot and then the name of the desired function
# i.e module_name.function_name   
# i.e pizza.make_pizza

# you can also import a specific function from a module using the syntax - from module_name import function_name 
# you can import as many functions are you want by comma seprating i.e from module_name import function_0, function_1, function_2
# when importing the function directly from a module, you don't need to use the dot notation between module name and function


# when importing a function you can give it an alias
# from pizza import make_pizza as mp
# mp(16, 'pepperoni')


def function_name(
        parameter_9,
        para
):
    print (para)


function_name('new', 'york')

# seperate each function in your program by two blank lines
# import statements should be written at the beginning of a file
