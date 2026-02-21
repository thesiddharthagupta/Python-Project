def c_to_f(c):
    return c*9/5 + 32

def f_to_c(f):
    return (f-32)*5/9

def km_to_mi(km):
    return km*0.621371

def mi_to_km(mi):
    return mi/0.621371

def kg_to_lb(kg):
    return kg*2.20462

def lb_to_kg(lb):
    return lb/2.20462


ops = {
    "1": ("C -> F", c_to_f),
    "2": ("F -> C", f_to_c),
    "3": ("KM -> MI", km_to_mi),
    "4": ("MI -> KM", mi_to_km),
    "5": ("KG -> LB", kg_to_lb),
    "6": ("LB -> KG", lb_to_kg),
}

while True:
    print("\n------ UNIT CONVERTER -------")

    # Print menu
    for k, (name, _) in ops.items():
        print(f"{k}. {name}")

    choice = input("Choose (q to quit): ")

    if choice.lower() == "q":
        print("Exiting Unit Converter...")
        break

    if choice in ops:
        val = float(input("Enter value: "))
        name, fn = ops[choice]
        result = fn(val)
        print(f"{name}: {val} -> {result:.2f}")
    else:
        print("Invalid choice!")