#input
# electricity 
#food rent
#electricity rate
#output 
#total amt to pay
#split

rent = int(input("Enter Rent amount: "))
food = int(input("Enter Food amount: "))
electricity_spend = int(input("Enter total of Electricity spend: "))
charge_par_unit = int(input("Enter the charge par unit: "))
member = int(input("Enter the number of Member to split: "))

total_bill = electricity_spend * charge_par_unit

split = (food + rent + total_bill) // member

print("Each person to pay: ", split)