def wrapper(f):
    def fun(l):
        num_list = []
        for number in l:
            if len(number) == 10:
                num_list.append("+91" + ' ' + number[0:5] + ' ' + number[5 :10])
            if len(number) == 11:
                num_list.append("+91" + ' ' + number[1:6] + ' ' + number[6: 11])
            if len(number) == 12:
                num_list.append("+91" + ' ' + number[2:7] + ' ' + number[7:12])
            if len(number) == 13:
                num_list.append("+91" + ' ' + number[3:8] + ' ' + number[8:13])
        f(num_list)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
