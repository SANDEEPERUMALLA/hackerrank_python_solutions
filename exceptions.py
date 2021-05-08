n = int(input())

while n > 0:
    a, b = input().split()
    try:
        result = int(a) // int(b)
        print(result)
    except ValueError as e:
        print("Error Code:", e)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    n -= 1
