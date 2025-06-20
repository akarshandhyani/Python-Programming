# This Video is based on  More Modes of File IO(Handeling) in Python like readlines() and writelines() methods

# Eg-:1 

f= open('Testfile.py','r')
i=0
while True:
    i=i+1
    line=f.readline()       # readline Method
    if not line:
        break
    m1 = line.split(",") [0] 
    m2 = line.split(",") [1] 
    m3 = line.split(",") [2] 
    print(f"Marks Of Student {i} in Maths is : {m1}")
    print(f"Marks Of Student {i} in Science is : {m2}")
    print(f"Marks Of Student {i} in SSt is : {m3}")
    
# writeline Method

# Eg-2

f=open('Testfile.py','w')
lines =['line1\n','line2\n','line3\n']
f.writelines(lines)
f.close()                                     

# O/P of vThe Above Program i.e. Eg-2 == line1
#                                        line2 
#                                        line3 