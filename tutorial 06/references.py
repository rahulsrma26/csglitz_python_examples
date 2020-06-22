colors = ['red', 'green', 'blue']
new_colors = colors
print('same', colors is new_colors)
print(f'{colors=} {new_colors=}')

new_colors = ['red', 'green', 'blue']
print('same', colors is new_colors)
new_colors[1] = 'yellow'
print(f'{colors=} {new_colors=}')
