import re

n = int(input())
while n > 0:
    string = input()
    match = bool(re.match(r'^[789][0-9]{9}$', string))
    if match:
        print('YES')
    else:
        print('NO')
    n -= 1
