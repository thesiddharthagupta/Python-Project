HISTORY_FILE = "History.txt"    #<- file name is in variable
def show_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            lines = f.readlines()

        if not lines:
            print("No history found!")
        else:
            print("\n----- History -----")
            for line in reversed(lines):
                print(line.strip())
            print("-------------------\n")

    except FileNotFoundError:
        print("No history f exists yet!")


def clear_history():
    with open(HISTORY_FILE, "w") as f:
        pass  # clears f safely
    print("History cleared!")


def save_to_history(equation, result):
    with open(HISTORY_FILE, "a") as f:
        f.write(f"{equation} = {result}\n")


def calculator(user_input):
    try:
        parts = user_input.split()

        if len(parts) != 3:
            print("Invalid format! Example: 5 + 3")
            return

        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            if num2 == 0:
                print("Cannot divide by zero!")
                return
            result = num1 / num2

        else:
            print("Invalid operator! Use + - * /")
            return

        if result.is_integer():     # remove decimal if integer
            result = int(result)

        print("Result:", result)

        save_to_history(user_input, result)

    except ValueError:
        print("Invalid number! Please enter valid numbers.")

    except Exception as e:
        print("Unexpected error:", e)


def main():
    print("===== Professional Calculator =====")
    print("Commands: history, clear, exit")
    print("Example calculation: 10 + 5\n")

    while True:
        user_input = input("Enter calculation or command: ").strip().lower()

        if user_input == "exit":
            print("Good Bye!")
            break

        elif user_input == "history":
            show_history()

        elif user_input == "clear":
            clear_history()

        else:
            calculator(user_input)


# start program
main()  #function call
