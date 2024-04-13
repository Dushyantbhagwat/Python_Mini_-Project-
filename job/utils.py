from datetime import datetime


def calculate_age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def is_password_strong(password):
    # Check for minimum length
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check for at least one special character (e.g., !@#$%^&*)
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?"
    if not any(char in special_characters for char in password):
        return False

    # All checks passed, the password is strong
    return True


# Minimum length of 8 characters.
# At least one uppercase letter.
# At least one lowercase letter.
# At least one digit.
# At least one special character from the provided set !@#$%^&*()-_=+[]{}|;:'\",.<>/?.
