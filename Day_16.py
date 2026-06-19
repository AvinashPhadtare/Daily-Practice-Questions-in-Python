def compress(s: str) -> str:
    if not s:
        return ""

    result = []
    count = 1
    current_char = s[0]

    for ch in s[1:]:
        if ch == current_char:
            count += 1
        else:
            if count >= 3:
                result.append(current_char + str(count))
            else:
                result.append(current_char * count)

            current_char = ch
            count = 1

    # Process the last run
    if count >= 3:
        result.append(current_char + str(count))
    else:
        result.append(current_char * count)

    return "".join(result)


# Exaple usage:
print(compress("aaabccddddee")) # a3bccd4ee 
print(compress("aabb")) # aabb 
print(compress("aaaa")) # a4 
print(compress("aabbbcc")) # aab3cc