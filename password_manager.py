def view():
    with open("passwords.txt", "r") as f:
        for line in f:
            name, pwd = line.strip().split("|")
            print("User:", name, "| Password:", pwd)


def add():
    name = input("Account Name: ").lower()
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("Add or view? (add/view), q to quit: ")

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
