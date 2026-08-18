#Write a program to demonstrate different 
#import mechanisms in Python. 

import math

print("--- normal import ---")
print(math.sqrt(25))


from math import factorial
print("--- function import ---")
print(math.factorial(5))


from math import *
print("--- * for all function of math ---")
print(floor(4.8))
print(trunc(7.89))
