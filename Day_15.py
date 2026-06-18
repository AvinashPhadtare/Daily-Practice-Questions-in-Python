def first_non_repeating_character(s: str):
    char_count = {}
    for ch in s:
        char_count[ch] = char_count.get(ch, 0) + 1
    for ch in s:
        if char_count[ch] == 1:
            return ch
    return -1
