'''15 Write a Python script to print a dictionary where the keys are numbers between
 1 and 15 (both included) and the values are square of keys.'''

A=dict()
for x in range(1,16):
    A[x]=x**2
print(A)