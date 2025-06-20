# This Video is based on Exception Handling in Python

# Eg-1

a=input("Enter a Number")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
    
except:
    print("Ye Kya Kar diya apne")
    
print ("Hello This is an Error")

# Eg-2

try:
    num=int(input("Enter A number: "))
except:
    print("ERROR....!  Please Enter A Numerical Value")