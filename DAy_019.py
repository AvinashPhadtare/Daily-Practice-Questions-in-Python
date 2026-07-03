def build_lps(pattern):
    lps = [0] * len(pattern)

    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def count_pattern_occurrences(text, pattern):
    if not pattern:
        return len(text) + 1

    lps = build_lps(pattern)

    i = 0  # text pointer
    j = 0  # pattern pointer
    count = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):
                count += 1
                j = lps[j - 1]   # allow overlapping matches

        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return count