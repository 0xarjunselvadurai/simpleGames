import random

def guessing_number_game():
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    max_attempts = 5  # Max number of attempts
    print("A number is chosen between 1 to 100. Guess the number within 5 trials.")

    for attempt in range(max_attempts):
        guess = int(input("Guess the number: "))  # Get the user's guess
        
        if guess == number_to_guess:
            print("Congratulations! You guessed the number.")
            break
        elif guess < number_to_guess and attempt != max_attempts - 1:
            print(f"The number is greater than {guess}.")
        elif guess > number_to_guess and attempt != max_attempts - 1:
            print(f"The number is less than {guess}.")

    else:
        print("You have exhausted 5 trials.")
        print(f"The number was {number_to_guess}.")

def main():
    guessing_number_game()

# Call the main function to run the game
if __name__ == "__main__":
    main()
