toss1 = input('Enter the result of your toss: ')
toss2 = input("Enter the result of your friend's toss (default: head): ")

if toss1 == 'head':
    if toss2 == 'head':
        print('You win!')
    else:
        print('tie')
        print('play again to break tie')
else:
    if toss2 == 'tail':
        print('You lose!')
    else:
        print('tie')
        print('play again to break tie')
