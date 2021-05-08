import re

n = int(input())

input_text = ''
while n > 0:
    input_text += input() + '\n'
    n -= 1


def replace_fn(match):
    m = match.group()
    if m == '&&':
        return 'and'
    elif m == '||':
        return 'or'

    pass


result = re.sub(r'(?<= )(\|\||&&)(?= )', replace_fn, input_text)
print(result)
