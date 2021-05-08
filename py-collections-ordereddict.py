from collections import OrderedDict

items_to_total_price_map = OrderedDict()

n = int(input())

while n > 0:
    *item, price = input().split()
    item_name = ' '.join(item)
    price_i = int(price)
    existing_total_price = items_to_total_price_map.get(item_name, 0)
    items_to_total_price_map[item_name] = existing_total_price + price_i
    n -= 1

for item in items_to_total_price_map:
    print(item, items_to_total_price_map.get(item))
