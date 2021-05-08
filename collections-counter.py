from collections import Counter

n = int(input())
shoe_sizes = list(map(int, input().split()))
customer_count = int(input())
size_to_count_map = Counter(shoe_sizes)

total_money = 0
while customer_count > 0:
    size, price = list(map(int, input().split()))
    available_quantity = size_to_count_map.get(size)
    if available_quantity:
        total_money += price
        size_to_count_map[size] = available_quantity - 1
    customer_count -= 1

print(total_money)
