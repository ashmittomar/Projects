import random


easy_words = ["apple", "train", "mango", "grapes", "tiger"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("Welcome to the Guessing Game!")
print("Choose a difficulty level: easy, medium or hard.")


level = input("Enter difficulty: ").lower()
if level == 'easy':
    secret = random.choice(easy_words)
elif level == 'medium':
    secret = random.choice(medium_words)
elif level == 'hard':
    secret = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to easy level.")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret word!")
print(f"Hint: {'_' * len(secret)}")


while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"\nCongratulations! You guessed it right in {attempts} attempts.")
        break

    
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Wrong guess. Try again!")
    print("Hint:", hint)

print("🎉 Game Over!")
