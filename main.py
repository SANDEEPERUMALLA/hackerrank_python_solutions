from collections import deque
from itertools import product


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⇧⌘B to toggle the breakpoint.


def func(n1, n2):
    print(n1, n2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
arr1 = ([1, 2, 3], [5, 6, 7])
print(list(product(arr1)))
