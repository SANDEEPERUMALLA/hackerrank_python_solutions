n, m = list(map(int, input().split()))
list_of_lists = [list(map(int, input().split())) for i in range(n)]
k = int(input())
list_of_lists.sort(key=lambda l: l[k])

for lst in list_of_lists:
    print(" ".join(list(map(str, lst))))
