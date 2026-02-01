import random
import string

def get_user_preferences():
    """Collect user preferences for password generation"""
    print("\nPassword Generator Settings")

    length = int(input("Enter desired password length (min 6): "))

    if length < 6:
        print("Password length must be at least 6.")
        return None

    include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    if not (include_upper or include_lower or include_digits or include_symbols):
        print("At least one character type must be selected.")
        return None

    return length, include_upper, include_lower, include_digits, include_symbols


def generate_password(length, upper, lower, digits, symbols):
    """Generate password based on selected options"""
    characters = ""

    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def password_strength(password):
    """Evaluate password strength"""
    strength = 0

    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    if len(password) >= 12:
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    else:
        return "Strong"


def main():
    print("=== Python Password Generator ===")

    try:
        preferences = get_user_preferences()
        if not preferences:
            return

        length, upper, lower, digits, symbols = preferences
        password = generate_password(length, upper, lower, digits, symbols)

        print("\nGenerated Password:", password)
        print("Password Strength:", password_strength(password))

    except ValueError:
        print("Invalid input. Please enter numeric values where required.")


if __name__ == "__main__":
    main()
