# This Video is based on Super Keyword in Python.
# (Part-2) The Super method refer class to the parent class

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
class Programmer(Employee):
    def __init__(self, name, id,Age):
        super().__init__(name, id)                   # Using This method our time is saved in writing self name and Age again.(Part-1)
        self.Age = Age
        
Rohan = Employee("Rohan Bhatt","21001")
Suraj = Programmer("Suraj Bhatt","21023","30")

print(Suraj.name)
print(Suraj.id)
print(Suraj.Age)