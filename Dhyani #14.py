# This video was was based on condition Statements.
# This video was based on condition operators.(<= , >= , == , != ,< , >)

# This is a example of a nested if else elif condition

num=int(input("Enter a number")) 
print("Thank you for the input")
if num>=18:
    print("you can drive")
    if num>=60:
        print("you are too big to drive")

elif num<=18:
    print("you cannot drive")
    if num<=10:
            print("you are too small to drive")


else:
    print("Error")
    