#program to reverse an Integer

def reverse_number(n):
    reversed_num = 0
    negative = n < 0
    n = abs(n)

    while n != 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return -reversed_num if negative else reversed_num


# Example usage
num = 12345
print("Original:", num)
print("Reversed:", reverse_number(num))
