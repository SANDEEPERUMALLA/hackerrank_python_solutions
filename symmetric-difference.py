m = int(input())
set1 = set(map(int,input().split()))
n = int(input())
set2 = set(map(int,input().split()))

for item in sorted(set1.difference(set2).union((set2.difference(set1)))):
    print(item)