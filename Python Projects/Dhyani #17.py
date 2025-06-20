# THis video was About For loops in python.

# Iterating over a string

name="Akarshan"
for i in name:
    print(i,end=",\n")
    
# Iterating over a List

colors=["Red","Green","Blue" ]
for x in colors:
    print(x,end=",")
    
# For Range

for K in range(5):
    print(K)
    
for K in range(5,1000):
    print(K)
    
for K in range(5,100,5):   # (Start, end, step)
    print(K)