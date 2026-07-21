def tokenize(expression: str):
    tokens = []
    i = 0

    while i < len(expression):
        current = expression[i]

        # Ignore spaces
        if current.isspace():
            i += 1
            continue

        # Build a number (integer or float)
        elif current.isdigit():
            number = ""
            dot_count = 0

            while i < len(expression) and (
                expression[i].isdigit() or expression[i] == "."
            ):

                if expression[i] == ".":
                    dot_count += 1

                    if dot_count > 1:
                        raise ValueError("Invalid float number")

                number += expression[i]
                i += 1

            tokens.append(("NUMBER", number))

        # Variable (single lowercase letter)
        elif current.islower():
            tokens.append(("VAR", current))
            i += 1

        # Operators
        elif current in "+-*/":
            tokens.append(("OP", current))
            i += 1

        # Left Parenthesis
        elif current == "(":
            tokens.append(("LPAREN", current))
            i += 1

        # Right Parenthesis
        elif current == ")":
            tokens.append(("RPAREN", current))
            i += 1

        # Invalid character
        else:
            raise ValueError(f"Invalid token: {current}")

    return tokens


# Example
expression = "3 + 42 * (x - 7.5)"

print(tokenize(expression))