"""Write a program to explain mutable and 
immutable objects in Python
"""

l = [1,2,3,4,5]
print(l)
print(type(l))
print(len(l))

l.append(6)
print(l)
print(len(l))

if(len(l)==6):
    print("mutable")
else:
    print("immutable")
    
t = (1,2,3,4,5)
print(t)
print(type(t))
