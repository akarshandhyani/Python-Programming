# This Video is based on 'Finally' Keyword in Python
# This is an Important keyword and below example is an ans of Ques. that why we need to use finally if we can print it simpliy?
# Because in some case like function it (simple print function at the end) can't work
# Eg.-1 (This Question is asked in Interviews)

def func1():
    try:
        l=[1,3,2,4]
        i=int(input("Enter the Index Value"))
        print(l[i])
        return 1
    except:
        print("Error.....!   Wrong Input Value")
        return 0
    finally:
        print("This Will Always Print")
        
x=func1()
print(x)