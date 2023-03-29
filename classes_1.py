class Resturant():
    """Modelling a resturant"""
    
    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 10


    
    def describe_resturant(self):
        print(f'The name of this resturant is called {self.resturant_name}')
        print(f'The cuisine they serve at {self.resturant_name} is called {self.cuisine_type}')


    def open_resturant(self):
        print(f'The {self.resturant_name} resturant is open')
        
    
    def set_number_served(self,customers):
        self.number_served = customers

    
    def increment_numbers_served(self,increase):
        self.number_served+= increase
    


resturant = Resturant('Mr Perri', 'irish')

resturant.set_number_served(23)

resturant.increment_numbers_served(10)

print(f'The number of customers we have served is {resturant.number_served}')



class User():
    """Builds a profile of a user"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f'The user first name is {self.first_name}')
    

    def greet_user(self):
        print(f'Good evening Mr {self.first_name} {self.last_name}')

    
    def increment_login_attempts(self):
        self.login_attempts += 1

    
    def reset_login_attempts(self):
        self.login_attempts = 0






zubby = User('Nzube', 'Mekah')
bilo = User('Emeka','Ezebilo')


zubby.increment_login_attempts()
zubby.increment_login_attempts()
zubby.increment_login_attempts()
zubby.increment_login_attempts()

zubby.reset_login_attempts()

print(f'The amount of login attempt is {zubby.login_attempts}')

