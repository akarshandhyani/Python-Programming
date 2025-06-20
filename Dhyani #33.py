# This Video is based on Dictionaries in Python

info={"name":"Dhyani","Age":19,"Eligibility":True}
print(info)
print(type(info))

# Accessing Items in Dictionary

print(info.keys())
print(info.values())

# Accessing Key Value Pairs

for key, value in info.keys():
    print(f"The value corresponding to {key} is {value}")
