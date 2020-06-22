from time import time

# How big the number is?
# Do we have enough memory?

a = list(range(1, 50_000))
print('Before', a[:10])

start = time()
b = []
for x in a:
    if x % 2 == 1: # it's odd
        b.append(x)
a = b
end = time()

print(' After', a[:10])
print('time taken', end - start, 'seconds')
