print("type 0 for NO ending the insert")


list1=[]

with open('yuvi.txt','w') as file1:
    while True :
        a = input("enter numbers : ")
    
        if a == '0':
            break
        else:
            print(a)
            list1.append(a)
    file1.write(str(list1))    


with open('yuvi.txt','r') as file2:
    b=file2.read()
    print(b)

'''
for i in range (100):
    
    a = input("enter numbers : ")
    
    if a == '0':
        break
    else:
        print(a)
        list1.append(a)
        
print(list1)
       
'''
