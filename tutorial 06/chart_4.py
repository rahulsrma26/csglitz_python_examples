n = int(input('Enter the number of subjects: '))
print('Enter subject and marks separated by space')
result = []
for i in range(n):
    subject, marks = input().split()
    result.append([subject, int(marks)])

print(f'{"Subject":>10} Marks')
for name, value in result:
    bar = '▇' * int(40 * value / 100)
    print(f'{name:>10} {value:03} {bar}')
