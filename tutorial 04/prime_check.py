n = int(input("Enter a number: "))

is_prime = False if n < 2 else True
for x in range(2, n):
    if n % x == 0:
        is_prime = False
        break

if is_prime:
    print("It's a prime number.")
else:
    print("Not a prime number.")
