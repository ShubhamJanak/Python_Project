import random
print('''Welcome to the Number Guessing Game!
You have 3 chance to guess number! Let's start!''')

low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))
print(f"you have 3 chances to guess the number between {low} and {high}")

num = random.randint(low, high)
guess_counter = 0
chances = 3

while guess_counter < chances:
    guess_counter += 1
    guess = int(input("Enter your guess: "))
    if guess == num:
        print(f"Congratulations! You guessed the number {num} correctly in {guess_counter} attempts.")
        break
    elif guess_counter >= chances and guess != num:
        print(f"Sorry! The number was {num}. Better luck next time!")
    elif guess > num:
        print("Too High! Try a lower number")
    elif guess < num:
        print("Too Low! Try a higher number")
            
