import re

roman_number = input()
match = re.match(r'[IVXLCDM]+', roman_number)
if match:
    print(True)
else:
    print(False)
