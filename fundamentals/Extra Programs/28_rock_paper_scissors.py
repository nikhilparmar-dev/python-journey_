import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    print("\n===== ROCK PAPER SCISSORS =====")
    print("Type: rock / paper / scissors")
    print("Type 'exit' to quit")

    user_choice = input("Enter your choice: ").lower()

    if user_choice == "exit":
        print("\nGame Over")
        print(f"Your Score: {user_score}")
        print(f"Computer Score: {computer_score}")
        break

    if user_choice not in choices:
        print("Invalid choice.")
        continue

    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a Draw!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1