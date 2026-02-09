print("Welcome to Ice-Cream Parlour!")
print("1. Vanilla Scope Ice-Cream - 80")
print("2. Strawberry Scope Ice-Cream - 90")
print("3. Chocolate Scope Ice-Cream - 110")
print("4. Mixed Scope Ice-Cream - 150")

total_bill = 0
orderMore = "yes"

while orderMore.lower() == "yes":
    choice = int(input("Please Choose (1-4): "))
    quantity = int(input("Enter Quantity: "))

    if choice == 1:
        total_bill += 80 * quantity
    elif choice == 2:
        total_bill += 90 * quantity
    elif choice == 3:
        total_bill += 110 * quantity
    elif choice == 4:
        total_bill += 150 * quantity
    else:
        print("Invalid choice!")
        continue

    orderMore = input("Do you want to order more? (Yes/No): ")

tax = total_bill * 0.08
final_bill = total_bill + tax

print("\n------------ BILL ------------")
print("Total before tax:", total_bill)
print("8% Tax:", tax)
print("Final Bill Amount:", final_bill)
print("-----------------------------")
print("Thank you for visiting our Ice Cream Parlour!")
