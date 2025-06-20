# This Video is based on Using For loops with Else in Python
# Else tabhi execute hota hai jab loop complete (pura) ho jaye,warna nahi chalega

# Eg:

i=0
for i in range(5):
    print(i)
    if i==3:
        break
else:
    print("Out of Loop")
    
    
# Eg-2

for x in range(7):
    print("iteration no {} in for loop".format(x+1))
else:
    print("Else block in loop")
    print("Out of Loop")