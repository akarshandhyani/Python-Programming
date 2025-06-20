# This video is based on Tuples in python
# It is Enclosed in round brackets { () }
# Values inside a tuple cannot be changed.
# Else Each and Every function is same as Lists

tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))

# List Index

print(tup[0])

# Negative LIst index

print(tup[-1])
print(tup[2])
# print(tup[34])

# Check wheather item is present in list or not

if  3421 in tup:
  print("Yes 342 is present in this tuple")
  
# Range of index

tup2 = tup[1:4]
print(tup2)