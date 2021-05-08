def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        substr = string[i: i + k]
        char_list = list(substr)
        s = set()
        unique_char_list = [ch for ch in char_list if ch not in s and not s.add(ch)]
        print(''.join(unique_char_list))


merge_the_tools('AABCAAADA', 3)
