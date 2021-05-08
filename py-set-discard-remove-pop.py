n = int(input())
s = set(map(int, input().split()))
command_count = int(input())


def process_command(s, args):
    if args[0] == 'remove':
        try:
            s.remove(int(args[1]))
        except KeyError as e:
            pass
    elif args[0] == 'discard':
        s.discard(int(args[1]))
    elif args[0] == 'pop':
        try:
            s.pop()
        except KeyError as e:
            pass


while command_count > 0:
    command_and_number = input().split()
    process_command(s, command_and_number)
    command_count -= 1
print(sum(s))
