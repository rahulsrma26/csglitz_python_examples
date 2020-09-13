
text = input()

unique_words = {word.lower() for word in text.split(' ')}

stop_words = {'is', 'a', 'the'}

print(unique_words - stop_words)
