import classes_1, classes
from classes import ElectricCar
from classes_1 import Resturant, User

class IceCreamStand(Resturant):
    """Defining an Icecream resturant that inhertits resturant"""
    
    def __init__(self, resturant_name, cuisine_type):
        super().__init__(resturant_name, cuisine_type)
        self.flavors = ['vanilla', 'coffee', 'rasberry']


    def dispaly_flavors(self):
        print('The ice cream flavors we have are: ')
        for flavor in self.flavors:
            print(f'\n {flavor}')



gellatos = IceCreamStand('Gellato','Desert')
gellatos.dispaly_flavors()
gellatos.describe_resturant()


class Admin(User):
    """Definig an admin user that inherits attributes from User"""
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.priviledges = Priviledges()

    
class Priviledges():
    """Creating a priviledges class that will become an attribute of User"""
    def __init__(self):
        self.priviledges = ['can post', 'can delete post', 'can ban user']


    def show_priviledges(self):
        print('The admin user has the following priviledges: ')
        for priviledge in self.priviledges:
            print(f'{priviledge}')



user_type = Admin('Nzube','Mekah')
user_type.priviledges.show_priviledges()

new_car = ElectricCar('Tesla','Model s', '2023')
new_car.battery.get_range()
new_car.battery.upgrade_battery()
new_car.battery.get_range()

