#Write a program to demonstrate conditional
#statements using if if-else and if-elif-else.

a=int(input('Enter Ai marks out of 100:'))
b=int(input('Enter Python marks out of 100:'))
print('-------------------------------------')

if a>=35 and b>=35:
    print('Passed in Both')
else:
    print('Failed in Both')

print('-------------------------------------')

if a>=35 and a<50:
    print('C grade in AI')
elif a>=50 and a<75:
    print('B grade in AI')
elif a>=0 and a<35:
    print('Failed in AI')
elif a>=75 and a<=100:
    print('A grade in AI')
else:
    print('enter valid marks of AI')
    
print('-------------------------------------')

if b>=35 and b<50:
    print('C grade in Python')
elif b>=50 and b<75:
    print('B grade in Python')
elif b>=0 and b<35:
    print('Failed in Python')
elif b>=75 and b<=100:
    print('A grade in Python')
else:
    print('enter valid marks of Python')
