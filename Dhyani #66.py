# This video is based on Instance Variable and Class Variables.
#  #67 is the solution video to Exercise 6
#  #68 is EX-7 (Which is to be done)

class Employee:
    companyName ="Apple"
    noofemployee = 0
    def __init__(self,name):
        self.name= name
        self.salaryraise_amount = 0.2
        Employee.noofemployee +=1
    def showdetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noofemployee} sized {self.companyName} is {self.salaryraise_amount}")
        
emp1= Employee("Akarshan")
emp1.salaryraise_amount= 0.4
emp1.companyName="Google"
emp1.showdetails()
    
emp2= Employee("Yobo")
emp2.salaryraise_amount= 0.7
emp2.companyName="Parle"
emp2.showdetails()
    