import re

n = int(input())

lines = ''
while n > 0:
    lines += input() + "\n"
    n -= 1

result = re.findall('(?<=[: ,])(#[0-9ABCDEF]{3}|#[0-9ABCDEF]{6})(?=[, ;)])', lines, re.IGNORECASE)
print("\n".join(result))
