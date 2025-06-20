# THis Video is Based on Class Methods in Python

class Employee:
    company = "Apple"
    def show(self):
        print (f"The Name is {self.name} and Company is {self.company}")
        
    @classmethod
    def changecompany(cls,newcompany):
        cls.company = newcompany
        
        
e1 = Employee()
e1.name = "Dhyani"
e1.show()
e1.changecompany("Google")
e1.show()
print(Employee.company)