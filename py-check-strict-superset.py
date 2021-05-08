set1 = set(map(int, input().split()))
n = int(input())

result = True
while n > 0:
    set2 = set(map(int, input().split()))
    result = result & (set1.union(set2) == set1 and len(set1) > len(set2))
    if not result:
        break
    n -= 1

print(result)
