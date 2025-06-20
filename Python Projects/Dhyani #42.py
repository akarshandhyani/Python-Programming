# This Video is based on Enumerate Function in Python
# Using This Build in function we can get index and value of each element in sequence at same time 
# Eg-:

fruits=["apple","Grapes","Mango"]
for index,fruit in enumerate(fruits):
    print(index,fruit)
    
# Eg-:2 Changing The Starting Index

Marks=[12,34,25,67,9,30,57,99]
for index,mark in enumerate(Marks,start=1):
    print(index,mark)
