# This Video was Based on Tuples operation.
# This can be done 3 Steps-:
# 1. Change Tuple into Lists
# 2. Make Change in List 
# 3. Change It back To Tuple 

# Example -:

Countries=("India","Bhutan","Russia")
temp=list(Countries)
temp.append("USA")       # Add item
temp.pop(3)       # Remove item
temp[2]="Finland"        # Change item
temp=tuple(Countries)
print(Countries)

# Methods 

# 1. Count

admin=(1,2,3,2,1,3,1,2,4,8)
avy = admin.count(3)
print("Index No of Req. Tuple is",avy)


# 2.Index

avz=admin.index(3,1,6)        # (Element,Start,End)
print(avz)


# 3. Length

ava=len(admin)
print(ava)