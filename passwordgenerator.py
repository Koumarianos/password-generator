import random
import string

def generate_password(length, use_special_chars, use_digits, use_uppercase):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    characters = lowercase
    if use_uppercase:
        characters += uppercase
    if use_digits:
        characters += digits
    if use_special_chars:
        characters += special_chars

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the length of the password: "))
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_special_chars, use_digits, use_uppercase)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
