# in OOP you write classes that represent real world things and situations and you create objects based on these classes
# making an object from a class is called instantiation and you would generally be working with instances of classes
# a function that is part of a class is called a method

class Dog():
    """A simple attempt to model a dog """

    def __init__(self, name, age): # self is automatically passed in every instance as it gives the instance access to attributes
        """Initialize name and age attributes"""
        self.name = name #self.name is a variable storing the attribute name from the __init__ method
        self.age = age   #any variable prefixed with self is available to every instance as well as methods of this class

    
    def sit(self):
        """Simulate a dog sitting in response to a command. """
        print(self.name.title() + " is now sitting ")

    
    def roll_over(self):
        """Simulate rolling over in response to a command. """
        print(self.name.title() + "rolled over! ")



# making instances of the class Dog()

my_dog = Dog('willie', 6) # initialized an instance of the class Dog 

# to access an attribute of a class use the dot notation 
# remember .name and .age are now variables representing the attributes
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + "years old")

#we can also use the dot notaion to call methods from the class my_dog

my_dog.sit()


class Resturant():
    """Modelling a resturant"""
    
    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type

    
    def describe_resturant(self):
        print(f'The name of this resturant is called {self.resturant_name}')
        print(f'The cuisine they serve at {self.resturant_name} is called {self.cuisine_type}')


    def open_resturant(self):
        print(f'The {self.resturant_name} resturant is open')
        


resturant = Resturant('Mr Perri', 'irish')

your_resturant = Resturant('Nandos', 'british')

print(resturant.resturant_name)
print(resturant.cuisine_type)

resturant.describe_resturant()
your_resturant.describe_resturant()
resturant.open_resturant()




class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f'The user first name is {self.first_name}')
    

    def greet_user(self):
        print(f'Good evening Mr {self.first_name} {self.last_name}')




zubby = User('Nzube', 'Mekah')
bilo = User('Emeka','Ezebilo')

zubby.describe_user()
zubby.greet_user()
bilo.describe_user()
bilo.greet_user()


# setting a default value for an attribute
# if you specify a value for an attribute in the body of the init function, the attribute does not need to be in the parameter when calling an instance

#e.g


class Car():

    def __init__(self,make, model, year):
        """Initialize attributes to make a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   #default value for attribute

    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car had {self.odometer_reading} miles on it")


my_newcar = Car('audi', 'ap4', '2016')
my_newcar.read_odometer() 


#modifying attribute values

# you can modify an attribute directly through the instance calling it 
my_newcar.odometer_reading = 23
# you can modify an attribute by updating it through a method

def update_odometer(self,mileage):
    """Set the odometer reading to a given value"""
    self.odometer_reading = mileage  #updating the attribute within the method


my_newcar.update_odometer(23)


#Inheritance
#If you are writing a class that is a specialized version of an earlier class you wrote, you can use inheritance
#when a class inherits from another, it usually takes all the attriibutes and methods of the first class. The child class inherits from the parent class but it is also free to define its own attributes and methods

#inheriting from class Car
# a parent class must be part of the file with the child class and most appear before it in the file 
class ElectricCar(Car): # parent class included in parantheses
    """Represents aspects of a car, specific to electric vehicles"""
    
    def __init__(self, make, model, year): #information required to make a ELectric Car instance
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year) #links parent to child
        # defiing different attributes for the child class
    #     self.battery_size = 70

    
    # def describe_battery(self):
    #     """Print a statement describing battery size"""
    #     print(f'This car has a {self.battery_size}-KWH battery')

        self.battery = Battery()


# my_tesla = ElectricCar('tesla','model s', 2016) #inherits super class attributes
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()


#Overiding methods
# to do this create a method with the same name as the method you are inheriting that you want to change. That is, you will create the same module name in the subclass(child)

#Sometimes you might notice a class has too many methods and will want to break those methods and attributes into a class of their own

# then in the class you want to use this class, you can call an instance of the class as an attribute


class Battery():
    """ Trying to make the battery attribute referenced a class"""

    def __init__(self,battery_size = 70):
        self.battery_size = battery_size
    
    
    def describe_battery(self):
        """Print a statement describing battery size"""
        print(f'This car has a {self.battery_size}-KWH battery')


    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go to approximately " + str(range) 
        message += " miles on a full charge."
        print(message)   
    

    def upgrade_battery(self):
        if self.battery_size:
            self.battery_size = 85

 



# we can now call this class as an attribute in class Electriccar by just writing self.battery = Battery()
# now to call a method within it, you would write my_tesla.battery.describe_battery()



