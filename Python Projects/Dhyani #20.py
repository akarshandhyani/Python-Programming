# This Video is based on Functions in Python
# They are declared by Def Keyword
# Space ka bohot imp role hai python mei 


def JMean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
    
def isGreater(a,b):
    if(a>b):
        print("A is greater than B\n")
    else:
        print("B is greater than A\n")
    
a = int(input("Enter the value of A\n"))
b = int(input("Enter the value of B\n"))

JMean(a, b)
isGreater(a, b)
