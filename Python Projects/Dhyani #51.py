# This Video is based on  More Functions of File IO(Handeling) in Python like seek() , tell() and truncate functions

# Seek Function()
# Eg-:

with open('TestFile.py','r') as f:
    print(type(f))
# Move to the 10th Byte in the file
    f.seek(10)

# Read next 5 bytes
    data=f.read(5)
    print(data)
    
    
# Tell Function ()

with open('TestFile.py','r') as f:
    print(type(f))
    
# Move to the 10th Byte in the file
    f.seek(5)
    print(f.tell())
    data=f.read(5)
    print(data)


# Truncate Function

with open('TestFile.py','w') as f:
    f.write('Hello World !')
    f.truncate(5)
    
with open('TestFile.py','r') as f:
    print(f.read())
        