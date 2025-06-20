# This Video is based on Time Module in Python

import time

# time.time() function

def usingWhile():
    i = 0
    while i<5000:
        i = i+1
        print(i)

def usingFor():
    for i in range(5000):
        print(i)
    
init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
t2 = time.time() - init
print(t1)
print(t2)
print(time.time())

# time.sleep() function

print(4)
time.sleep(3)
print("This is printed after 3 Seconds")



# time.strftime() function

t = time.localtime()
formatted_time = time.strftime("%Y-%M-%D %H:%M:%S", t)

print(formatted_time)
