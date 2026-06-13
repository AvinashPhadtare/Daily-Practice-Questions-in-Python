def password_strength(password: str):
    l = len(password)
    new_password = password.strip()

    if l > 8 or (new_password.isalpha or new_password.isdigit) and "!@#$%^&*" in new_password:
        return "strong"
    
    if l > 6 or (new_password.isalpha() and new_password.isdigit()):
        return "medium"
    
    if l < 6 or new_password.isalpha():
        return "weak"
    
    

# Example usage :- 
print(password_strength("abc"))     # output ->  weak
print(password_strength("avinash1"))    # ouput -> medium 
print(password_strength("Avinash@1"))   # output -> strong 