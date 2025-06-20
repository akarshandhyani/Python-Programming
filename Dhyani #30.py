# This Video is Based on Recurrsion fuction in python
# Recursion ka Matlab Function ke Ander function call karna

# Eg-: 1. Finding Factorial of a Number

def factorial(num):
    if (num==0 or num==1):
        return 1
    else:
        return(num*factorial(num-1))

# Calling Function

num=5
print("Number",num)
print("Factorial",factorial(num))

# Also for Fibonacci

def fibonacci(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    elif (n>1):
        return(fibonacci(n-1)+fibonacci(n-2))

# Calling Function

n=9
print("Number",n)
print("Fibonacci",fibonacci(n))
