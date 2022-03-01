def make_word_list(filename):
    with open(filename, encoding='unicode_escape') as f:
        list_of_words = []
        for line in f:
            word = line.strip().lower()
            list_of_words.append(word)
        return list_of_words


main_word_list = make_word_list('ukenglish.txt')
