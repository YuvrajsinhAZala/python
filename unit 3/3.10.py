#Write a program to extract specific information 
#from a text file using regular expressions.

import re

obj = re.compile(r'\d+')

str1 = 'hello 7678789797'

result = obj.search(str1)

print(result.group())
