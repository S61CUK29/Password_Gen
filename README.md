# Password_Gen
Password generator
 Random Password Generator – Python Script
This Python script generates secure, customizable passwords with options for length and character types. It's useful for creating simple passwords, strong passwords, or numeric PINs on the fly.

 Features:
Adjustable password length

Toggle options for including:

 Uppercase letters

Digits
 Special characters (e.g., !@#$%)

Ensures minimum complexity by including at least one character from each selected category.

Shuffles characters for unpredictability.

 Dependencies:
Uses only Python’s built-in random and string modules (no external libraries required).

 Example Usage:
python
Copy
Edit
# Simple 8-character password with letters and digits
generate_password(length=8, use_special=False)

# Strong 16-character password with all character types
generate_password(length=16)

# 4-digit numeric PIN
generate_password(length=4, use_uppercase=False, use_special=False, use_digits=True)
 Sample Output:
yaml
Copy
Edit
Simple Password: f6LtzhnG
Strong Password: %YWm@TGP47)EKD!0
Numeric PIN: 3741
