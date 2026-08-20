#Write a program to demonstrate basic regular 
#expression pattern matching.

#import re

#prog = re.compile(r'm\w\w')

#str = 'cat mat rat bat'

#result = prog.search(str)

#print(result.group())


import re

prog = re.compile(r'm\w\w')

str = input('enter string :')

result = prog.search(str)

if result:
    print(result.group())
else:
    print('match not found')
