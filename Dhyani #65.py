# This Video is Based on Static Methods in Python
# Eg-:

class Math:
    def __init__(self,num):
        self.num = num
    
    def addtonum(self,n):
        self.num=self.num+n
        
    @staticmethod
    def add(a,b):
        return a+b

a=Math(5)
print(a.num)
a.addtonum(5)
print(a.num)

# Using Static method
        
print(a.add(7,4))

# Using Class Name 
print(Math.add(7,4))        