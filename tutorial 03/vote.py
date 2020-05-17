age = int(input("Enter your age in years: "))

if age < 18:
    print("You cannot vote yet")
    print(f"You have to wait {18 - age} years.")
else:
    print("You can vote")
