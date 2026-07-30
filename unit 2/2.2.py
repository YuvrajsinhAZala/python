#Write a program to check whether a number is
#positive negative or zero using nested conditions.

num=float(input('Enter a number : '))

if num>=0:
    if num==0:
        print('number is zero')
    else:
        print('number is positive')
else:
    print('number is negative')

'''
if num>0:
    print(num,'is Positive')
elif num<0:
    print(num,'is negative')
else:
    print('number is zero')
'''
