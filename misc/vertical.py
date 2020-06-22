result = [
    ['English', 72],
    ['Maths', 93],
    ['Physics', 82],
    ['Chemistry', 67]
]

# we will print everything in a list of strings
height = 30
width = 10
# width of the string depends upon number of subjects
line = ['│'] + [' '] * (len(result) * width)
screen = [line.copy() for _ in range(height)]

# put marks in the middle
yaxis = 'Marks'
yoffset = int((height - len(yaxis)) / 2)
for i, v in enumerate(yaxis):
    screen[i + yoffset][0] = v

for i, (_, marks) in enumerate(result):
    h = int(height * marks / 100)
    for j in range(h):
        for k in range(width - 2):
            screen[height - 1 - j][i * width + 2 + k] = '█'
    c = int((width - len(str(marks))) / 2)
    for j, v in enumerate(str(marks)):
        screen[height - 1 - h][i * width + 1 + c + j] = v

# print chart
for row in screen:
    print(''.join(row))

# print x axis
print('└─' + 'Subjects'.center(len(result) * width, '─'))
xaxis = [subject.center(10) for subject, _ in result]
print('  ' + ''.join(xaxis))
