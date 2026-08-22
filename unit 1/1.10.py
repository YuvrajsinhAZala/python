'''10.Write a program to demonstrate recursion using 
factorial or Fibonacci series. '''

           
def fibo(n):
    if n<=1:
        return 1
    return fibo(n-1)+fibo(n-2)
re=fibo(5)
print(re)

# Recursive function to find factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a number: "))

result = factorial(num)

print("Factorial of", num, "is", result)
