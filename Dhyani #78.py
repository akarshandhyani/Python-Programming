# THis Video is based on Single Inheritance in Python

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound Made by Animal")
        
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark")
        
d = Dog("Dog","Pitbull")
d.make_sound()

a = Animal("Dog","Dog")
a.make_sound()