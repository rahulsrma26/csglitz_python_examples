a = (-1, 2, -2, 1, 0)
print('data', a)

b = a[::-1]
print('reverse', b)

b = tuple(sorted(a))
print('sorted', b)

b = tuple(sorted(a, reverse=True))
print('sorted (reverse)', b)

b = tuple(sorted(a, key=abs))
print('sorted (abs)', b)

a = ((1,2), (1,), (2,), (), (1,3), (2,2), (1,2,1))
a = tuple(sorted(a))
print('tuple of tuple', a)
