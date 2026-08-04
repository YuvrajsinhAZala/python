#Write a program to find the sum of digits of a
#number using a while loop.

num = int(input('enter number :'))
summ=0


while(num>0):
    a=num%10
    summ=summ+a
    num=num//10
print(summ)
