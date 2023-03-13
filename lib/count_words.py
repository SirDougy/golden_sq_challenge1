def count_words(text):
    word_count = len(text.split(' '))
    return word_count


r = count_words('are flaps fuck nasty poo')
print(r)
