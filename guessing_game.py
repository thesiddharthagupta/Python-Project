import random

easy_words = ["apple","banana","orange","pinapple"]
medium_words = ["python", "Aeroplane", "helicopter", "elephant", "Umbrella"]
hard_words = ["kumfu", "gymnastic", "enlightments", "commplicated"]

print("Welcome to the password guessing game!")
print("Choose a Difficulty Level: easy, medium or Hard ")


level = input("Enter difficulty: ").lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid Choice. defaullting to easy level")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret password!")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"Congratulation! You guessed it in {attempts} attempts.")
        break

    hint = ""
    for i in range (len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
    
    print("Hint: ", hint)
print("Game Over!")