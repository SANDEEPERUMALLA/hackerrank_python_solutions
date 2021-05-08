from collections import OrderedDict

n = int(input())

word_to_count_map = OrderedDict()

while n > 0:
    word = input().strip()
    c_count = word_to_count_map.get(word, 0)
    word_to_count_map[word] = c_count + 1
    n -= 1

print(len(word_to_count_map))
for item in word_to_count_map:
    print(word_to_count_map[item], end=' ')

