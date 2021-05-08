from collections import defaultdict

m, n = list(map(int, input().split()))

empty_list = []
a_map = defaultdict(list)
index = 1
while m > 0:
    element = input().strip()
    a_map[element].append(index)
    index += 1
    m -= 1

while n > 0:
    element = input().strip()
    if element in a_map:
        print(' '.join(list(map(str, a_map[element]))))
    else:
        print(-1)
    n -= 1
