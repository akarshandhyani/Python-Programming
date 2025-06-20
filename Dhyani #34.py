# This Video is based on Dictionaries Methods in Python

# update()

info = {'name':'Dhyani', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

# Removing items from dictionary:

# clear():

info = {'name':'Dhyani', 'age':19, 'eligible':True}
info.clear()
print(info)

# pop():

info = {'name':'Dhyani', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

# popitem():

info = {'name':'Dhyani', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

# del:

# Case - 1 If key is Provided

info = {'name':'Dhyani', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

# Case - 2 If key is not provided, then the del keyword will delete the dictionary entirely.

info = {'name':'Dhyani', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)        # It Will Show Error as no dictionary Exists now
