from datetime import datetime, timedelta

n = int(input())

while n > 0:
    t1 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    print(int(abs((t1 - t2).total_seconds())))

    n -= 1
