# list to tuple to list
a = [1, 2, 3]
b = tuple(a)
print(b)
c = list(b)
print(c)

# get a modified tuple using slicing
a = tuple(range(5))
print(a)
b = a[:2] + (9,) + a[3:]
print(b)
