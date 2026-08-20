#Write a program to use re module functions 
#such as match search and find all. 




#import re

#prog = re.compile(r'm\w\w')

#str = 'cat mat rat bat'

#result = prog.search(str)

#print(result.group())


import re

prog = re.compile(r'm\w\w')

str1 = input('enter string :')

result = prog.search(str1)
result1 = prog.findall(str1)
result2 = prog.match(str1)

if result:
    print(result.group())
    print(result1)
    print(result.group())
else:
    print('match not found')
