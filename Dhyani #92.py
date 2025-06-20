# This Video is based on Function Catching in Python

# Eg-:

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("Done For 20")
print(fx(2))
print("Done For 2")
print(fx(6))
print("Done For 6")
print(fx(14))
print("Done For 14")

# Now Since the cache is stored in the memory now so when we call the same values,
# we get all frequently without recomputing as they are stored in current memory

print(fx(20))
print("Done For 20")
print(fx(2))
print("Done For 2")
print(fx(6))
print("Done For 6")
print(fx(14))
print("Done For 14")

# But for this value cause it is new, the compliler will 5 seconds again
print(fx(30))
print("Done For 30")