# THis Video is based on Hybrid and Hierarchical Inheritance in Python

# Hybrid Inheritance

class Baseclass:
    pass

class Derived1(Baseclass):
    pass

class Derived2(Baseclass):
    pass

class Derived3(Derived1,Derived2):
    pass


# Hierarchical Inheritance

class Baseclass:
    pass

class D1(Baseclass):
    pass

class D2(Baseclass):
    pass

class D3(D1):
    pass

class D4(D2):
    pass