# This video is based on Decorators in Python.

def greet(fx):
    def mfx(*args, **kwargs):
        print("Hello User")
        fx(*args, **kwargs)
        print("THank You For Working With Us")
    return mfx

@greet

def hello():
    print("Hello World")

@greet   
def sum(a,b):
    print(a+b)
    
hello()
sum(2,4)
    