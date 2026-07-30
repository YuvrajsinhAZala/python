"""Write a program to create a dictionary and 
demonstrate dictionary methods and iteration. 
"""
y = {1:"abc",
     2:"ijk",
     3:"xyz"
     }
print(y)

print(y.keys())
print(y.values())
print(y.items())

for i in y.keys():
    print (i)
    
for i in y.values():
    print (i)


for i in y.items():
    print (i)
