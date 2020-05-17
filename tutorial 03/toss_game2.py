toss1 = input('Enter the result of your toss: ')
toss2 = input("Enter the result of your friend's toss: ")

if toss1 == 'head' and toss2 == 'head':
    print('You win!')
elif toss1 == 'head' or toss2 == 'head':
    print('tie')
    print('play again to break tie')
else:
    print('You lose!')
