#program to generate fibnacci series using list comprehension

# Generate Fibonacci series using list comprehension

n = 20  # Number of Fibonacci terms

# Using list comprehension with a loop and temporary variables
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(n - 2)]

print(f"Fibonacci series with {n} terms:")
print(fibonacci)
