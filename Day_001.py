def is_valid_username(username: str):
    if len(username) < 5 or len(username) > 15:
        return False
    
    if not username[0].isalpha():
        return False
    
    for ch in username:
        if not (ch.isalpha() or ch.isdigit() or ch =="_"):
            return False
        
    if username[-1] == "_":
        return False
    
    return True


# Example usage:-
string = input("Enter a username: ")
print(is_valid_username(string))
