# This video is based on Access Modifiers in Python.
# It is 3 Types -:


# 1. Public Access Modifiers
# Eg-:

class Employee:
    def __init__(self):
        self.name = "Arpit"
        
a = Employee()
print(a.name)



# 2. Private Access Modifiers
# Eg-:

class Student:
    def __init__(self):
        self.__name = "Aman"
    
a = Student()

# print(a.__name) # Cannot be accessed directly

print(a._Student__name) # Can be accessed directly

print(a.__dir__())



# 3. Protected Access Modifiers
# Eg-:

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())


