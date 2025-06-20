# This video is based on Lists in Python

marks=[2,3,"Dhyani","akarshan",23,45,10,1000]
print(marks)
print(type(marks))

# List Index

print(marks[2])
print(marks[0])
print(marks[4])

# Negative LIst index

print(marks[-2])
print(marks[-3])

# Check wheather item is present in list or not

if 2 in marks:
    print("Yes")
else:
    print("No")

# Range of index
    
print(marks[1:4:1])

# List Coprehension

lst=[i for i in range(5)]
print(lst)

lst=[i*i for i in range(5)]
print(lst)

# With Condition

lst=[i*i for i in range(5) if i%2==0]
print(lst)