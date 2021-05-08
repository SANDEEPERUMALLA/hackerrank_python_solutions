import re

for i in range(int(input())):
    card = input().strip()
    isValidCardNumber = bool(re.match(r'^[456][0-9]{3}[-]?[0-9]{4}[-]?[0-9]{4}[-]?[0-9]{4}$',
                                      card))
    card_with_just_numbers = card.replace('-', '')
    areNumbersRepeating = bool(re.search(r'([0-9])\1{3,}', card_with_just_numbers))
    if isValidCardNumber and not areNumbersRepeating:
        print('Valid')
    else:
        print('Invalid')
