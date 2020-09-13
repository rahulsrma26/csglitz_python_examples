
a = set(range(5))

print('Before', a)

a.add(-5)
a.remove(3)

print('After', a)

a.clear()

print('Clear', a)
