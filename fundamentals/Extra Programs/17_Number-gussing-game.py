import random

# Computer chooses a random number between 1 and 10
target_number = random.randint(1, 10)

print("I have chosen a number between 1 and 10. Try to guess it!")

# Loop runs forever until the user guesses correctly
while True:
    try:
        # Take user guess
        guess = int(input("Enter your guess: "))
        
        # Check the guess
        if guess < 1 or guess > 10:
            print("Please guess a number within the 1-10 range!")
        elif guess > target_number:
            print("Too High! Try again.")
        elif guess < target_number:
            print("Too Low! Try again.")
        else:
            print("Correct! You won!")
            break  # Stops the loop when the guess is correct
            
    except ValueError:
        print("Invalid input! Please enter a valid whole number.")
