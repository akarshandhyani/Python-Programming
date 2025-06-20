# This Video is based on File IO(Handeling) in Python

# Opening a File
'''
Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.

Here's an example of how to open a file for reading:

f = open('myfile.txt', 'r')

By default, the open() function returns a file object that can be used to read from or write to the file, depending on the mode.'''

# Modes in file
'''

1. read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

2. write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

3. append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

4. create (x): This mode creates a file and gives an error if the file already exists.

5. text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

6. binary (b): used to handle binary files (images, pdfs, etc).

'''

# Reading from a File

'''
f = open('myfile.txt', 'r')
contents = f.read()
print(contents)
'''

# Writing to a File

'''
f = open('myfile.txt', 'w')
f.write('Hello, world!')
'''

# Keep in mind that writing to a file will overwrite its contents. If you want to append to a file instead of overwriting it, you can open it in append mode.
'''
f = open('myfile.txt', 'a')
f.write('Hello, world!')
'''

# Closing a File
# It is important to close a file after you are done with it. This releases the resources used by the file and allows other programs to access it.
# To close a file, you can use the close() method.

'''
f = open('myfile.txt', 'r')
# ... do something with the file
f.close()
'''


# The 'with' statement
# Alternatively, you can use the with statement to automatically close the file after you are done with it.

'''
with open('myfile.txt', 'r') as f:
    # ... do something with the file
'''


# Now The code done by harry


# f = open('Testfile.py', 'r')
# text = f.read()
# print(text)
# f.close()

# Writing a File

f = open('Testfile.py', 'w')
f.write("Hello World !")
f.close()

# With Statement

with open('Testfile.py','a') as f:
    f.write("Hello Akarshan Dhyani")