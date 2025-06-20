# This Video is Based on F-strings in python

# Earlier this was used to format string in python

letter="Hello my name is {} and I m from {}"
name="Akarshan"
dharm="Sanatan Dharm"
print(letter.format(name,dharm))

# Now using f-string in python

print(f"Hello my name is {name} and I am from {dharm}")

# These double {{}} are used to print curly brackets in our python output terminal

print(f"Hello my name is {{name}} and I am from {{dharm}}")

#Some More Examples of F-string

price=49.0999
print(f"For only price {price:.2f}") #.2f shows only upto 2 decimal values

#also

print(f"{2*40}")