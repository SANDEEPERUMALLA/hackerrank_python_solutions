m, n = list(map(int, input().split()))
list1 = list(map(int, input().split()))
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

happiness = 0
for item in list1:
    if item in set1:
        happiness += 1
    elif item in set2:
        happiness -= 1
print(happiness)
