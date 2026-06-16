def find_anagram_groups(words):
    groups = {}

    for word in words:
        # Create a unique key for all anagrams
        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    # Keep only groups having more than one word
    result = []

    for group in groups.values():
        if len(group) > 1:
            result.append(group)

    return result


# Test
words = ["eat", "tea", "tan", "ate", "nat", "bat", "gym", "listen", "silent"]

print(find_anagram_groups(words))