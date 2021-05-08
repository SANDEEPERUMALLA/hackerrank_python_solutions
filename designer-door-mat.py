import math
n, m = list(map(int, input().split()))
print(n, m)


def pf(i):
    return '-' * i


def pf_middle(count):
    return '.' + '..'.join(list(('|' * count))) + '.'


count = 1
for i in range(1, n + 1):

    if i < math.ceil(n / 2):
        _count = (m - (count + (count - 1) * 2 + 2)) // 2
        left = pf(_count)
        middle = pf_middle(count)
        right = pf(_count)
        print(left + middle + right)
        count += 2
    elif i > math.ceil(n / 2):
        count -= 2
        _count = (m - (count + (count - 1) * 2 + 2)) // 2
        left = pf(_count)
        middle = pf_middle(count)
        right = pf(_count)
        print(left + middle + right)
    else:
        _count = (m - 7) // 2
        left = pf(_count)
        middle = 'WELCOME'
        right = pf(_count)
        print(left + middle + right)
