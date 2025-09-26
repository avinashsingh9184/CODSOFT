import random
import string

def password_generator():
    print("---- Password Generator ----")
    
    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print(" Password length should be at least 4 characters for security!")
            return

        print("\nChoose complexity level:")
        print("1. Only Letters (a-z, A-Z)")
        print("2. Letters + Numbers")
        print("3. Letters + Numbers + Symbols")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            characters = string.ascii_letters
        elif choice == "2":
            characters = string.ascii_letters + string.digits
        elif choice == "3":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            print(" Invalid choice! Defaulting to Letters + Numbers + Symbols.")
            characters = string.ascii_letters + string.digits + string.punctuation

        password = "".join(random.choice(characters) for _ in range(length))
        print(f"\n Generated Password: {password}")

    except ValueError:
        print(" Please enter a valid number for length!")


password_generator()