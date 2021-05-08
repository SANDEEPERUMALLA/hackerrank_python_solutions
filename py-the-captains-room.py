from collections import Counter
K = int(input())
room_numbers = list(map(int, input().split()))
room_numbers_to_count_map = Counter(room_numbers)

for room_number in room_numbers_to_count_map:
    if room_numbers_to_count_map[room_number] == 1:
        print(room_number)
