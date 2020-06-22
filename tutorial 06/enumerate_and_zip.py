fruits = ['Apple', 'Banana', 'Orange']
numbers = [1, 3, 2]

print('List of fruits to buy:')
for i, (fruit, number) in enumerate(zip(fruits, numbers), 1):
    print(f'{i}. {fruit} x{number}')
