def get_nr_of_words(sentence):
    words = sentence.split()
    return len(words)

print(get_nr_of_words("apple, banana, cherry"))