import random

def get_user_choice():
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        return "rock"
    elif choice == "2":
        return "paper"
    elif choice == "3":
        return "scissors"
    else:
        return None


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user, computer):
    if user == computer:
        return "Draw"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "User"
    else:
        return "Computer"


def main():
    print("=== Rock Paper Scissors Game ===")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()

        if user_choice is None:
            print("Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "User":
            print("You win this round!")
            user_score += 1
        elif result == "Computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("This round is a draw.")

        print(f"\nScore → You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()
