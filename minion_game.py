def minion_game(string):
    n = len(string)
    vowels = {'A', 'E', 'I', 'O', 'U'}
    word_count_with_vowels = 0
    word_count_with_consonants = 0

    for i in range(0, n):
        if string[i] in vowels:
            word_count_with_vowels += n - i
        else:
            word_count_with_consonants += n - i

    if word_count_with_consonants > word_count_with_vowels:
        print("Stuart", word_count_with_consonants)
    elif word_count_with_consonants > word_count_with_vowels:
        print("Kevin", word_count_with_vowels)
    else:
        print("Draw")

minion_game('BANANA')