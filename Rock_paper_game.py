import random

emojis = {"r": "🪨", "p": "📃", "s": "✂️"}
choices = ("r", "p", "s")

user_score = 0
computer_score = 0

while True:
    user_choice = input("Rock, paper or scissors? (r/p/s or q to quit): ").lower()

    if user_choice == "q":
        print("\nGame Over!")
        print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
        break

    if user_choice not in choices:
        print("Invalid Choice!")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    # ---- Winner Logic ----
    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "p" and computer_choice == "r") or
        (user_choice == "s" and computer_choice == "p")
    ):
        print("You Win! 🎉")
        user_score += 1

    else:
        print("Computer Wins! 💻")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}")
    print("-" * 30)
