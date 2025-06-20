# THis video is based on dir() , __dict__ and Help Methods in Python

# Dir() Method

x=[1,2,3,4]
print(dir(x))
print(x.__add__)



# __dict__ Method

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
p = Person("YOBO",30)
print(p.__dict__)



# Help Method

print(help(Person))