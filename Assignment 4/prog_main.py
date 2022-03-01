import sys

from auto_correcet import AutoCorrect
from word_list import *
from alphabet import *
from freq_dict import *
"""In this program, the user is to write a word and get three best suggestions based on the probability of bigrams. 
If the word is typed in incorrectly, the suggestions for a possible correct word based on the edit distance 
of 1 is proposed to choose from"""


# a method for searching the bigrams and suggesting the 3 most probable
def search_for_word(bigram_dic, in_word, list_suggest):
    list_s = []  # the final list after adding the sorted bigrams
    for k1, k2 in bigram_dic:
        if k1 == in_word:
            list_suggest[k1, k2] = bigram_diction[k1, k2]  # making a bigram dictionary based on entery
    for x, y in sorted(list_suggest, key=list_suggest.get, reverse=True):  # sorting and adding first three to a list
        list_s.append(y)
    return ', '.join(list_s[:3])


#  The main menu for giving suggestions
if __name__ == "__main__":
    list_of_suggestion = defaultdict(int)
    auto_correct = AutoCorrect(main_word_list, alpha)
    bigram_diction = make_dict('UNv1.0.testset.en')
    while True:
        input_list = []  # saving a list of the words users has written
        main_input = input('Vill du testa ett ord här:\n')  # the first input
        if main_input.lower() == 'ja':  # if the user wants to start texting
            print('Skriv ett ord på engelska här:\n')  # the first word
            in_w = input('')
            if in_w in main_word_list:
                input_list.append(in_w)
                k = search_for_word(bigram_diction, in_w, list_of_suggestion)
                print(k)
                v_word = input('välj ditt nästa ord: ')  # asking for the next word
                input_list.append(v_word)
                if v_word in k:
                    search_for_word(bigram_diction, v_word, list_of_suggestion)
                else:  # if the wordis not among the suggested words
                    print(f'har tyvärr inga flera förslag för ordet: {v_word} ')
                    print(' '.join(input_list))
                    main_input = v_word  # going back to the first input
            else:  # if the word is misspelled
                print(f' Ordet finns inte i listan, \nMenade du: {auto_correct.return_set(in_w)}')
        elif main_input.lower() != 'nej':  # if the user writes something unclear for starting the texting process
            second_input = input('Va lite mer tydligt, tack: \n')
            main_input = second_input
        else:  # if the user does not want to start texting
            sys.exit()
