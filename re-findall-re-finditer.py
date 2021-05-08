import re

result = re.findall(
    r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])',
    input(), re.IGNORECASE)

if len(result) == 0:
    print(-1)
else:
    print('\n'.join(result))
