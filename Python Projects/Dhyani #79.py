# THis Video is based on Multiple Inheritance in Python

# Eg-: 1

class Employee:
    def __init__(self, name):
        self.name = name
        def show(self):
            print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance
        
        def show(self):
            print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name

ab = DancerEmployee("Kathak", "Shivani")
print(ab.name)
print(ab.dance)
#ab.show()              # Its showing Error Needs to be Checked
print(DancerEmployee.mro())