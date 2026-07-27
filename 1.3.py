a=int(input('value of A :'))
b=int(input('value of B :'))

#arithmetic 
add=a+b
sub=a-b
multi=a*b
div=a/b

print('sum is =',add)
print('sub is =',sub)
print('multi is =',multi)
print('div is =',div)


#relational
print('A equals B = ',a==b)
print('A not equals B = ',a!=b)
print('A is greater B = ',a>b)
print('A is less then B = ',a<b)
print('A >= B',a>=b)
print('A <= B',a<=b)


#logical

if(a>=0 and a<=10):
    print('A is in the range of 0 to 10')
else:
    print('A is not in the range of 0 to 10')


if(a>=0 or a<5):
        print('A is in the range of 0 to 10')
else:
    print('A is not in the range of 0 to 10')


if(not(a<5)):
        print('A is in the range')
else:
    print('A is not in the range ')



