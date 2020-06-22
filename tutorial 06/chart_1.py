names = ['English', 'Physics', 'Chemistry', 'Maths']
marks = [76, 81, 68, 92]

print(f'{"Subject":>10} Marks')
for i in range(len(names)):
    bar = '▇' * int(40 * marks[i] / 100)
    print(f'{names[i]:>10} {marks[i]:03} {bar}')
