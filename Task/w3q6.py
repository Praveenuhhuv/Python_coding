password = input("Enter your password: ")
length_check = len(password) >= 8
uppercase_check = any(char.isupper() for char in password)
lowercase_check = any(char.islower() for char in password)
digit_check = any(char.isdigit() for char in password)
special_char_check = any(char in "!@#$%^&*()-_+=" for char in password)

if length_check and uppercase_check and lowercase_check and digit_check and special_char_check:
    print("Password is valid.")
else:
    print("Invalid password")
    if not length_check:
        print("- Password must be at least 8 characters long.")
    if not uppercase_check:
        print("- Password must contain at least one uppercase letter (A-Z).")
    if not lowercase_check:
        print("- Password must contain at least one lowercase letter (a-z).")
    if not digit_check:
        print("- Password must contain at least one digit (0-9).")
    if not special_char_check:
        print("- Password must contain at least one special character (!@#$%^&*()-_+=).")
