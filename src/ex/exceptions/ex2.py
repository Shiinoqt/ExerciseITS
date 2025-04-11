def validate_password(password:str):
    if len(password) <= 20:
        raise ValueError("Password must be at least 20 characters long.")
    
    uppercase_count = 0

    for char in password:
        if char == char.upper():
            uppercase_count += 1

    if uppercase_count < 3:
        raise ValueError("Password must contain at least 3 uppercase letters.")



password = input("Enter a password: ")

validate_password(password)