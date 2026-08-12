#10.Write a program to generate a sequence of 
#numbers using generator functions and yield keyword.


def func1(i):
    while i>0:
        yield i
        i-=1

for i in func1(5):
    print(i)
