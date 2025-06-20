# This Video is based on Lambda Function in Python

# Instead of Writing This-:
# def Double(x):
# Return X*2
# # We Use lambda Function
# Also We Can also make a function in a function in python 
# For Eg-:

def appl(fx,value):
    return 10+fx(value)


double = lambda x : x*2
cube = lambda x: x*x*x
avg = lambda x,y,z: (x+y+z)/3

print(double(9))
print(cube(5))
print(avg(1,2,3))
print(appl(double,10))