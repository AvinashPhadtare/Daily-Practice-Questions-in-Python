def password_strength(password: str):
    has_letter = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.isalpha():
            has_letter = True
        elif ch.isdigit():
            has_digit = True
        elif ch in "!@#$%^&*":
            has_special = True

    if len(password) >= 8 and has_letter and has_digit and has_special:
        return "strong"
    elif len(password) >= 6 and has_letter and has_digit:
        return "medium"
    else:
        return "weak"


print(password_strength("Avinash@!1"))  # Output: strong
print(password_strength("avinash123"))        # Output: medium  
print(password_strength("abc"))          # Output: weak