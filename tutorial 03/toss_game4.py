toss1 = input('Enter the result of your toss (default: head): ') or 'head'
toss2 = input("Enter the result of your friend's toss (default: head): ") or 'head'

if toss1 == 'head' == toss2:
    print('You win!')
elif toss1 == toss2:
    print('You lose!')
else:
    print('tie')
    print('play again to break tie')
