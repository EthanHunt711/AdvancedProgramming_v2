import sys

from nltk import tokenize
from auto_correcet import AutoCorrect
from word_list import *
from alphabet import *
from freq_dict import *

def menu(in_word):
    print(f'nej{in_word}')


if __name__ == "__main__":
    list_of_suggestion = []
    auto_correct = AutoCorrect(main_word_list, alpha)
    bigram_diction = make_dict('swedish_blog_sentences.txt')
    while True:
        main_input = input('Vill du testa ett ord här:\n')
        if main_input.lower() == 'ja':
            print('Skriv ett ord på engelska här:\n')
            in_w = input('')
            if in_w in main_word_list:
                for (k1, k2) in sorted(bigram_diction, key=bigram_diction.get, reverse=True):
                    if in_w == k1:
                        list_of_suggestion.append((k1, k2))
                        for (x, y) in list_of_suggestion[:3]:
                            print(y)
            else:
                print(f' Menade du: {auto_correct.return_set(in_w)}')
        elif main_input.lower() != 'nej':
            second_input = input('Va lite mer tydligt, tack: \n')
            main_input = second_input
        else:
            sys.exit()



