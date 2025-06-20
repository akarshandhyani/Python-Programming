# This video was based on Lists Methods in Python

l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)

# append():

l.append(7)

# list.sort()

l.sort(reverse=True)

# reverse()

l.reverse()

# index()

print(l.index(1))

# count()

print(l.count(1))

# copy()

m = l.copy()

# insert():

m[0] = 0
l.insert(1, 899)

# Concatenating two lists:

m = [900, 1000, 1100]
k = l + m
print(k)

# extend():

l.extend(m)
print(l)