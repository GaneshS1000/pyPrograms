# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
print(sys.path)
sys.path.insert(0,"C:\\Users\\Ganesh S\\PycharmProjects")
print(sys.path)
from testmod import myFun

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
myFun()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
