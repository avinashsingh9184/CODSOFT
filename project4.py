import random

def rock_paper_scissors():
    print("---- Rock-Paper-Scissors Game ----")
    choices = ["rock", "paper", "scissors"]

    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose one: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()

        if user_choice not in choices:
            print(" Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f" You chose: {user_choice}")
        print(f" Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print(" It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print(" You win this round!")
            user_score += 1
        else:
            print(" Computer wins this round!")
            computer_score += 1

        print(f" Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n Thanks for playing Rock-Paper-Scissors!")
            print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print(" You are the overall winner!")
            elif user_score < computer_score:
                print(" Computer is the overall winner!")
            else:
                print(" It's an overall tie!")
            break

rock_paper_scissors()