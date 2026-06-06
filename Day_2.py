def longest_substring(string: str):
    start = 0
    max_len = 0
    seen = set()


    for i in range(len(string)):

        while string[i] in seen:
            seen.remove(string[start])
            start = start + 1

        seen.add(string[i])
        length = i - start + 1
        if length > max_len:
            max_len = length



    return max_len


print(longest_substring("abcabcbb"))  # → 3
print(longest_substring("bbbbb"))     # → 1
print(longest_substring("pwwkew"))    # → 3
print(longest_substring("avinash"))   # → 6
