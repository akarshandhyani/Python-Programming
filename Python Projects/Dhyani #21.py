# This Video was based on Function Arguements in python.

# Default arguments:

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")

# Keyword arguments:

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")

# Required arguments:

# Eg. - 1

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Quill","Singh")

# Eg. - 2

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")

# Variable-length arguments:

# 1. Arbitrary Arguments:

def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")

# 2. Keyword Arbitrary Arguments:

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

# Return Statement

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))