import random
import string

def generate_password(length):
    # Define possible character sets
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # Special characters like @, #, $

    # Combine all characters
    all_chars = letters + digits + symbols

    # Ensure at least one letter, digit, and symbol
    password = random.choice(letters) + random.choice(digits) + random.choice(symbols)

    # Fill the rest of the password with random characters
    password += ''.join(random.choice(all_chars) for _ in range(length - 3))

    # Shuffle to avoid predictable order
    password_list = list(password)
    random.shuffle(password_list)

    return ''.join(password_list)

def main():
    try:
        length = int(input("Enter desired password length (min 6): "))
        if length < 6:
            print("⚠️ Password length should be at least 6.")
        else:
            password = generate_password(length)
            print(f"\n🔑 Generated Password: {password}")
    except ValueError:
        print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    main()
