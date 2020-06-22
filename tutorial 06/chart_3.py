n = int(input('Enter the number of subjects: '))
names = []
print('Enter the name of the subjects one by one')
for i in range(n):
    names.append(input())

marks = []
for i in range(n):
    value = int(input(f'Enter marks in {names[i]}: '))
    marks.append(value)

print(f'{"Subject":>10} Marks')
for name, value in zip(names, marks):
    bar = '▇' * int(40 * value / 100)
    print(f'{name:>10} {value:03} {bar}')
