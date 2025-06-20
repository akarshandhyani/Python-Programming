# This video is based on Constructors in Python.

# Eg:

class Person:
    def __init__(self,name,occ):
        print("This is an Example Of Parameteric Constructors")
        self.name= name
        self.occ= occ

    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a=Person("Akarshan","Student")
b=Person("Aman","Athelete")
print(a.name)
print(b.name)
print(a.occ)
print(b.occ)
a.info()
b.info()

