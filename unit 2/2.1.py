#Write a program to demonstrate conditional
#statements using if if-else and if-elif-else.

a=int(input('Enter A value :'))
b=int(input('Enter B value :'))

if a>b:
    print('A is greater')
else:
    print('B is greater')

print('-------------------------------------')

if a>b:
    print('A is greater')
elif a==b:
    print('A and B are Equal')
else:
    print('B is greater')
