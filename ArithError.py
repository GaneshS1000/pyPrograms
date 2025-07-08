try:
    y = 1 / 0

except (ArithmeticError,ZeroDivisionError):
    print("Arithmetic problem!")
    print("Zero Divison Error")

print("THE END.")
