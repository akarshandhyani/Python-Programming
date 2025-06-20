# This Video is Based on Method Overriding In Python

class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def area(self):
        return self.x*self.y
    
# This can be done using THis also        
''' 
    
class Circle:
    def __init__(self,radius):
        self.radius = radius
 
    def area(self):
        return 3.14*self.radius*self.radius
        
'''
# This can be done using THis Super Method also 
 
class Circle:
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius)
 
    def area(self):
        return 3.14 * super().area()  
    

rec = Shape(4,5)     
c = Circle(5)
print(c.area())
    
