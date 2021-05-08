import re

for i in range(int(input())):
    number = input().strip()
    isValidFloatingPointNumber = bool(re.match(r'^[-+]?[0-9]*[.][0-9]+$', number))
    if isValidFloatingPointNumber:
        print('True')
    else:
        print('False')
