
#  a method for making a list of lexicon based on a given file
def make_word_list(filename):
    with open(filename, encoding='unicode_escape') as f:  # the encoding of utf-8 could not be used
        list_of_words = []
        for line in f:
            word = line.strip().lower()
            list_of_words.append(word)
        return list_of_words


# the main word list for using in the main program
main_word_list = make_word_list('ukenglish.txt')
