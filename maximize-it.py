from itertools import product

k, n = list(map(int, input().split()))

lists = [tuple(map(int, input().split()))[1:] for _ in range(0, k)]

max_sum = -1
for lst in product(*lists):
    s = sum([ele ** 2 for ele in lst]) % n
    if max_sum < s:
        max_sum = s

print(max_sum)
