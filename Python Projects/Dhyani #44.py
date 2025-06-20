# This Video is based on How Import Works in Python
# Eg-:

import math
result=math.sqrt(9)
print(result)

# From Keywords

from math import sqrt,pi
result=sqrt(9)
print(pi)
print(result)

# The 'as' Keyword

import math as m
result=m.sqrt(9)
print(result)

# imoprting Everthing

from math import *
result=math.sqrt(9)
print(result)

# The 'Dir' Function

import math
print(dir(math))

# Another Example Of Import Function

from TestFile import add
# print(add)