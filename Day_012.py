def is_palindrome(s: str) -> bool:
    cleaned = ""

    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()

    left = 0 
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        
        left += 1
        right -= 1

    return True

# Test cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False
print(is_palindrome(""))  # True
print(is_palindrome(" "))  # True
print(is_palindrome("0P"))  # False
    