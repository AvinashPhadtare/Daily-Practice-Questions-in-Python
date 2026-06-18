def first_non_repeating_character(s: str):
    char_count = {}
    for ch in s:
        char_count[ch] = char_count.get(ch, 0) + 1
    for ch in s:
        if char_count[ch] == 1:
            return ch
    return -1


# Exaple usage:
print(first_non_repeating_character("abacabad"))  # Output: 'c'
print(first_non_repeating_character("abacabaabacaba"))  # Output: -1
print(first_non_repeating_character("z"))  # Output: 'z'
print(first_non_repeating_character("bcb"))  # Output: 'c'  
print(first_non_repeating_character("bcccccccb"))  # Output: 'b'