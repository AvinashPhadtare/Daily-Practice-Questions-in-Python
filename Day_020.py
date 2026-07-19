def validate_json_string(s: str) -> bool:
    valid_escape_seq = {'"', '\\', 'n', 't', 'r'}

    # String must start and end with double quotes
    if len(s) < 2 or s[0] != '"' or s[-1] != '"':
        return False

    i = 1  # Skip the opening quote

    while i < len(s) - 1:  # Stop before the closing quote
        current = s[i]

        # Raw newline is not allowed
        if current == '\n':
            return False

        # Found an escape sequence
        if current == '\\':

            # '\' cannot be the last character before closing quote
            if i + 1 >= len(s) - 1:
                return False

            next_char = s[i + 1]

            # Check whether the escape sequence is valid
            if next_char not in valid_escape_seq:
                return False

            # Skip both '\' and the escaped character
            i += 2
            continue

        # Normal character
        i += 1

    return True


# Test cases
print(validate_json_string('"hello"'))             # True
print(validate_json_string('"say\\"hi\\""'))       # True
print(validate_json_string('"bad\\edvspe"'))       # False
print(validate_json_string('""'))                  # True
print(validate_json_string('"hello\\nworld"'))     # True
print(validate_json_string('"hello\nworld"'))      # False
print(validate_json_string('"abc\\'))              # False