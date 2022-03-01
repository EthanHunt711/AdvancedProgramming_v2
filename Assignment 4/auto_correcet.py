"""A class for making corrections to the words misspelled based on edit distance 1"""


class AutoCorrect:
    def __init__(self, word_list, alpha):
        self.word_list = word_list
        self.alpha = alpha

    def insertion(self, word):  # if one character extra is inserted at any position
        words_of_insertion = []
        for al in self.alpha:
            for i in range(len(word) + 1):
                word_i = word[:i] + al + word[i:]
                if word_i in self.word_list:
                    words_of_insertion.append(word_i)
        return words_of_insertion

    def deletion(self, word):  # if the input misses one character
        words_of_deletion = []
        for i in range(len(word)):
            del_word = word[:i] + word[i+1:]
            if del_word in self.word_list:
                words_of_deletion.append(del_word)
        return words_of_deletion

    def substitution(self, word):  # if a character is substituted mistakenly with another
        words_of_subs = []
        for al in self.alpha:
            for i in range(len(word)):
                sub_word = word[:i] + al + word[i+1:]
                if sub_word in self.word_list:
                    words_of_subs.append(sub_word)
        return words_of_subs

    def swapping(self, word):  # if a character is swapped with the neighboring
        words_of_swap = []
        for i in range(len(word)-1):
            l_1 = word[i:i+1]
            l_2 = word[i+1:i+2]
            swa_word = word[:i] + l_2 + l_1 + word[i+2:]
            if swa_word in self.word_list:
                words_of_swap.append(swa_word)
        return words_of_swap

    def return_set(self, word):  # all possible words with edit distance 1 are created and listed out
        edit_one = []
        edit_one.append(self.insertion(word))
        edit_one.append(self.deletion(word))
        edit_one.append(self.substitution(word))
        edit_one.append(self.swapping(word))
        for word_l in edit_one:  # a loop for avoiding empty lists
            if len(word_l) > 0:
                return ', '.join(word_l)
