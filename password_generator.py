import string
import random

def generate_password(length, upper_case, numbers, special_char):
    if length < (upper_case + numbers + special_char):
        raise ValueError("Password length is too short for the specified criteria.")

    password = ""

    if upper_case:
        password += random.choice(string.ascii_uppercase)
    if numbers:
        password += random.choice(string.digits)
    if special_char:
        password += random.choice(string.punctuation)

    characters = string.ascii_lowercase
    if upper_case:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if special_char:
        characters += string.punctuation

    for _ in range(length - len(password)):
        password += random.choice(characters)

    password_list = list(password)
    random.shuffle(password_list)
    return "".join(password_list)


def main():
    length = int(input("Enter password length: "))
    upper_case = input("Include upper case letters? (y/n) ").lower() == "y"
    numbers = input("Include numbers? (y/n) ").lower() == "y"
    special_char = input("Include special characters? (y/n) ").lower() == "y"
    try:
        password = generate_password(length, upper_case, numbers, special_char)
        print(password)
    except ValueError as e:
        print(e)





if __name__ == "__main__":
    main()
