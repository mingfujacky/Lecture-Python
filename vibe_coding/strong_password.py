"""
A strong password should include at least one symbol and one digit and one lowercase character and one uppercase character.
return True if the password is strong, False if not.
"""
def is_strong_password(password):
    if len(password) < 8:
        return False
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)
    return has_upper and has_lower and has_digit and has_symbol 

"""
keep asking user for passwords until they enter a strong password return the strong password.
"""
def get_strong_password():
    while True:
        password = input("Enter a strong password: ")
        if is_strong_password(password):
            return password
        print("Weak password. Please try again.")

get_strong_password()