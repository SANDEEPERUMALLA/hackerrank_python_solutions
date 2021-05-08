from calendar import weekday, day_name
m, d, y = list(map(int, input().split()))
print(day_name[weekday(y, m, d)].upper())

