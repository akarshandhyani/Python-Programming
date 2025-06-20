# #47 was a solution video to Ex-4 which is done in #40
# This Video is based on Local Vs Global Variable in Python

x=10  # Global Variable
print(x)

def my_function():
    global x
    x=12 # This will change the value of local variable 'x'
    y=5 #Local Variable
    print(y)
    
my_function()
print(x)    # O/P == 12
print(y)    # This will Give an Error as 'y' is an local variable and is not accessible from outside the function    