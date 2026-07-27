class LogMixin:
    def log(self, message: str):
        print(f"[{self.__class__.__name__}] {message}")


class ValidatorMixin:
    def validate_email(self, email: str) -> bool:
        return "@" in email and "." in email

    def validate_phone(self, phone: str) -> bool:
        return phone.isdigit() and len(phone) == 10


class Member(LogMixin, ValidatorMixin):
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone

    def register(self):
        if self.validate_email(self.email) and self.validate_phone(self.phone):
            self.log("Registration successful")
            return True
        else:
            self.log("Registration failed")
            return False


# Example usage
# Example 1
member1 = Member("Avinash", "avi@gmail.com", "9876543210")
print(member1.register())

# Example 2
member2 = Member("Rahul", "rahulgmail.com", "98A654321")
print(member2.register())