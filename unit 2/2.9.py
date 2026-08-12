#Write a program to demonstrate iterators and 
#iterables in Python.


one=[10,20,30,40,50]

#print(dic1)
print('iterables')
for i in one:
    print(i)

print('=========================')
print('iterator')

def func1(i):
    while i>0:
        yield i
        i-=1

for i in func1(5):
    print(i)
