try:
    value = float(input("Enter value: "))
    assert value != 0  # can be shortened to assert value
    print("Reciprocal of the value is", 1 / value)
except AssertionError:
    print("Invalid value")