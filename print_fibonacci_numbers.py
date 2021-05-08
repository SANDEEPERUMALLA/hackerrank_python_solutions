cube = lambda x: x ** 3


def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    f_list = [0, 1]
    for i in range(2, n):
        f_list.append(f_list[i - 1] + f_list[i - 2])
    return f_list


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
