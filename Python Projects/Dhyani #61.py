# This video is based on Inheritance in Python.

# Eg-:

class Employee:                                                            # This is the Base Class
    def __init__(self, name, Id):
        self.name = name
        self.Id=d
        
    def Showdetails(self):
        print(f"Hello, My name is {self.name} and My Id is {self.Id} ")
        
class Programmer(Employee):                                                # This is the Child Class
    def showlanguage(self):
        print("The Default Language is Python")


e1 =Employee("Aman", 2100123)
e1.Showdetails()
e2 =Employee("Arpit", 2100120)
e2.Showdetails()


