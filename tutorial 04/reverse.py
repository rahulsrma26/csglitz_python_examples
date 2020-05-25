n = int(input("Enter a number: "))
r = 0

while n > 0:
    last_digit = n % 10
    r = r*10 + last_digit
    n //= 10

print(f"Reverse is {r}")
