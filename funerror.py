def myFun():
    return 0/0

try:
    myFun()
except :
    raise ZeroDivisionError
else:
    print("It's a value")