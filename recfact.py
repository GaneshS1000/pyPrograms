#program to find the factorial of a number using recursion

def fact(n):
    if n<=1:
        return 1
    else:
        return (n) * fact(n-1)
print("Enter the number")
n = int(input())
print("Factorial :",fact(n))