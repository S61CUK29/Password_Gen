import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    """
    Generate a random password with customizable complexity.
    
    Parameters:
    - length: int, length of the password (default: 12)
    - use_uppercase: bool, include uppercase letters (default: True)
    - use_digits: bool, include digits (default: True)
    - use_special: bool, include special characters (default: True)
    
    Returns:
    - str: generated password
    """
    characters = ""
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
        
    
    # Ensure password contains at least one character from each selected category
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    
    # Fill the rest with random characters
    remaining_length = length - len(password)
    password.extend(random.choice(characters) for _ in range(remaining_length))
    
    # Shuffle to mix the fixed characters
    random.shuffle(password)
    
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    print("Simple Password:", generate_password(length=8, use_special=False))
    print("Strong Password:", generate_password(length=16))
    print("Numeric PIN:", generate_password(length=4, use_uppercase=False, use_special=False, use_digits=True))