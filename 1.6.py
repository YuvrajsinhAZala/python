"""Write a program to illustrate the use of tuples 
and sets with basic operations."""

abc = ("a","b","c")

print(abc)
print(abc[0:2])
print(abc[1:3])
print(abc[0:2])

print("---------------")

tup = ("a","b","c")

y = list(tup)
y.pop(1)
z= tuple(y)
print(z)


print("-------------------------------------------")
print("-------- set ----------")

s ={1,2,3}
print(s)
print(type(s))


