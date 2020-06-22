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
for i in range(len(names)):
    bar = '▇' * int(40 * marks[i] / 100)
    print(f'{names[i]:>10} {marks[i]:03} {bar}')
