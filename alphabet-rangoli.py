def print_rangoli(size):
    n = size + size - 1
    total_length = n + n - 1
    # top part

    start_letter = 97 + size - 1
    end_letter = 97 + size - 1
    for i in range(0, size - 1):
        print_line(start_letter, end_letter, total_length)
        start_letter -= 1

    print_line(97, end_letter, total_length)

    start_letter = 98
    for i in range(0, size - 1):
        print_line(start_letter, end_letter, total_length)
        start_letter += 1


def print_line(start_letter, last_letter, total_length):
    string = chr(start_letter)
    current_charater = start_letter + 1
    while current_charater <= last_letter:
        string = chr(current_charater) + string + chr(current_charater)
        current_charater = current_charater + 1
    string = '-'.join(list(string))
    underscore_count_to_be_added = (total_length - len(string)) // 2
    final_str = ('-' * underscore_count_to_be_added) + string + "-" * underscore_count_to_be_added
    print(final_str)


print_rangoli(5)
