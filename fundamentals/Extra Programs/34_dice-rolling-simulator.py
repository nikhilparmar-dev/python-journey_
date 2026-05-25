import random

while True:
    input("Press Enter to roll the dice...")

    dice = random.randint(1, 6)
    print(f"You rolled: {dice}")

    choice = input("Roll again? (yes/no): ").lower()

    if choice != "yes":
        print("Game ended.")
        break
