password = "12abCD!$"

digits = lower = upper = special = 0
for ch in password:
    if ch.islower():
        lower += 1
    elif ch.isupper():
        upper += 1
    elif ch.isdigit():
        digits += 1
    elif ch in "!@#$%^&*":
        special += 1

if digits < 2:
    print("Password should have at least 2 digits")
elif lower < 2:
    print("Password should have at least 2 lowercase characters")
elif upper < 2:
    print("Password should have at least 2 uppercase characters")
elif special < 2:
    print("Password should have at least 2 special characters")
else:
    print("Good Password!")
