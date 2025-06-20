# This video is based on the Generators in Python

def my_generator():
    for i in range(500):
        # Complex Computations
        yield i 
        
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

# Also in a loop 

for j in gen:
    print(j)