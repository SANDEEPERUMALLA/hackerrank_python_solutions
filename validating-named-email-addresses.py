import re

n = int(input())
while n > 0:
    username, email = input().split()
    isValidEmail = bool(re.match('^[a-zA-Z0-9_\-.]+@[a-zA-Z]+\\.[a-zA-Z]{1,3}$', email[1: -1]))
    if isValidEmail:
        print(username, email)
    n -= 1
