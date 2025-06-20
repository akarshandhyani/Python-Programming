# This video is based on Classes and Objects in Python

# Eg-:

class Person:
    name="Harry"
    age=20
    occupation="Student"
    def information(self):
        print(f"{self.name} is {self.age} Years Old And is a {self.occupation}")
    

a=Person()
b=Person()
c=Person()

a.name="Sam"
a.age =28

b.name="Ambush"
b.age="22"

a.information()
b.information()
c.information()
