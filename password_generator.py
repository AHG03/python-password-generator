import string
import random

def generate_password(length, upper_case, numbers, special_char):
    characters = string.ascii_lowercase
    if upper_case:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if special_char:
        characters += string.punctuation

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password

def main():
    length = int(input("Enter password length: "))
    upper_case = input("Include upper case letters? (y/n) ").lower() == "y"
    numbers = input("Include numbers? (y/n) ").lower() == "y"
    special_char = input("Include special characters? (y/n) ").lower() == "y"
    password = generate_password(length, upper_case, numbers, special_char)
    print(password)




if __name__ == "__main__":
    main()
