n = int(input())
numbers = input().split()
print(all([int(num) > 0 for num in numbers]) & any([num == num[::-1] for num in numbers]))

