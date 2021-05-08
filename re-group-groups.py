import re
match = re.search(r'([A-Za-z0-9])\1+', input())
if match:
    print(match.group(1))
else:
    print(-1)