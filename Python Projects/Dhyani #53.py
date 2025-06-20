# This Video is based on Map , Filter and Reduce in Python

# Map 
# Eg -:
def cube(x):
    return x * x * x

print(cube(3))
# For A List we use map
l=[2,4,3,5,8,10]

newl=map(cube,l)
newl=list(map(cube,l))
print(newl)

# Filter
def Filter(a):
    return a>2

newnewl=list(filter(Filter,l))
print(newnewl)
    
    
# Reduce 

from functools import reduce

numbers=[10,20,30,40]

# Calculate the sum of Functions Using Reduce Function

def mysum(x,y):
    return x+y

sum=reduce(mysum,numbers)

# Print Sum
print(sum)
    