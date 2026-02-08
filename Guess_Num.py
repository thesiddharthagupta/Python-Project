import random 
num_to_guess = random.randint(1,100)
while True:
    try:
        guess = int(input("Enter the number between 1 and 100: "))
        if guess < num_to_guess:
            print("Too low!")
        elif guess > num_to_guess:
            print("Too high")
        else:
            print("Congratulation! You guessed the number.")
            break
    except ValueError:
        print("Please, Enter  a valid number.")
