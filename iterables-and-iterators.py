from itertools import combinations

word, kStr = input().split()
k = int(kStr)

final_combinations = []
for i in range(1, k + 1):
    for s in combinations(word, i):
        final_combinations.append(''.join(sorted(s)))

for comb in sorted(final_combinations, key=lambda x: (len(x), x)):
    print(comb)
