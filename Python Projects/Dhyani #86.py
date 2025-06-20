# This Video is based on Walrus Operator in Python
# Walrus Operator
# New to python 3.8
# Assignment expression aka Walrus Operator

# Eg-: 1


happy = False
print(happy)

#  Using Walrus

print(happy:= True)


# Eg-: 2

#  Using Normal Method 

Foods = list()
while True:
    Food = input("What Food do you Like ?:")
    if Food == "quit":
        break
    Foods.append(Food)
    
#  Using Walrus Method

foods = list()
while (food := input("What Food do you Like ?:")) != "quit":
    foods.append(food)
