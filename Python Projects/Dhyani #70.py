# THis video is based on Class MEthods as Alternative constructors.
# Instead of writing the whole code in the main area we just use class method and write our desired condition in it which makes the 
# code more readable and clean.

class Employee:
    def __init__(self,name,Salary):
        self.name=name
        self.Salary= Salary
        
        
    @classmethod
    def fromstring(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])               
    
e1=Employee("Dhyani",20000)
print(e1.name)
print(e1.Salary)

str="YOBO-25000"
e2=Employee.fromstring(str)
print(e2.name)
print(e2.Salary)