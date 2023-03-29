#Using Python Standard Library 

#OrderedDict orders a dictionary so it prints in order it was filled

from collections import OrderedDict
from random import randint

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")



class Die():

    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))
    


die_1 = Die(3)
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()


#check out http://pymotw.com/
