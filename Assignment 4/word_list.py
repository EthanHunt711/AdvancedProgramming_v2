def make_word_list(filename):
    with open(filename, encoding='utf-8') as f:
        list_of_words = []
        for line in f:
            word = line.strip().lower()
            list_of_words.append(word)
        return list_of_words


main_word_list = make_word_list('sv-utf8.txt')
