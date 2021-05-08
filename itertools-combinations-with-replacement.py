from itertools import combinations_with_replacement

word, kStr = input().split()
k = int(kStr)

final_combinations = []
for s in combinations_with_replacement(word, k):
    final_combinations.append(''.join(sorted(s)))

for comb in sorted(final_combinations, key=lambda x: (len(x), x)):
    print(comb)
