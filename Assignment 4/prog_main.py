import sys

from auto_correcet import AutoCorrect
from word_list import *
from alphabet import *
from freq_dict import *


def search_for_word(bigram_dic, in_word, list_suggest):
    list_s = []
    for k1, k2 in bigram_dic:
        if k1 == in_word:
            list_suggest[k1, k2] = bigram_diction[k1, k2]
    for x, y in sorted(list_suggest, key=list_suggest.get, reverse=True):
        list_s.append(y)
    return ', '.join(list_s[:3])


if __name__ == "__main__":
    list_of_suggestion = defaultdict(int)
    auto_correct = AutoCorrect(main_word_list, alpha)
    bigram_diction = make_dict('UNv1.0.testset.en')
    while True:
        input_list = []
        main_input = input('Vill du testa ett ord här:\n')
        if main_input.lower() == 'ja':
            print('Skriv ett ord på engelska här:\n')
            in_w = input('')
            if in_w in main_word_list:
                input_list.append(in_w)
                k = search_for_word(bigram_diction, in_w, list_of_suggestion)
                print(k)
                v_word = input('välj ditt nästa ord: ')
                input_list.append(v_word)
                if v_word in k:
                    search_for_word(bigram_diction, v_word, list_of_suggestion)
                else:
                    print(f'har tyvärr inga flera förslag för ordet: {v_word} ')
                    print(' '.join(input_list))
                    main_input = v_word
            else:
                print(f' Ordet finns inte i listan, \nMenade du: {auto_correct.return_set(in_w)}')
        elif main_input.lower() != 'nej':
            second_input = input('Va lite mer tydligt, tack: \n')
            main_input = second_input
        else:
            sys.exit()
