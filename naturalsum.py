#program to calculate the sum of natural numbers using recursion

def naturalSum(n):
    if n<=0:
        return 0
    else:
        return n + naturalSum(n-1)

print("Enter the range")
n = int(input())
print("Sum is :",naturalSum(n))