# This Video is based on Raising  Custom Errors In Python in Python
# Eg.-1
# Raising Custom errors 

salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

# Defining Custom Exceptions

# Syntax-:

class CustomError(Exception):
      # code ...
  pass

try:
  # code ...

except CustomError:
  # code...


