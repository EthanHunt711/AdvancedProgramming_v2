import sys
import time
from collections import defaultdict
from Bubble_sort import bubble_sort


class LexicalEntry:  # creating an object for the dictionary keys
    def __init__(self, lex):
        self.lex = lex

    def split_lex(self):  # splitting the object into letters and, after changing to lower case, saving them into a list
        split_list = []
        for le in self.lex:
            split_list.extend(le.lower())  # making the entry case insensitive
        return split_list

    def joined_sorted_lex(self):  # taking the list and turn it into an anagram
        s = self.split_lex()
        j_lex = bubble_sort(s)  # using bubble_sort() for sorting the letters
        s_lex = ''.join(j_lex)
        return s_lex


def word_to_list(word):  # a separate method for turning a word into anagram
    w_l = []
    for el in word.lower():
        w_l.append(el)
    return ''.join(bubble_sort(w_l))


def make_dict_keys(opened_file):  # creating the dictionary keys which returns a dictionary with keys and
    # empty lists as values
    anagram_dict = defaultdict(list)  # a defaultdict for saving objects as keys
    with open(opened_file, encoding='utf8') as s:  # opening a file
        for lex_entry_line in s:  # looping the file for entries into dictionary
            w = lex_entry_line.strip()
            u = LexicalEntry(w)  # creating a instance of the object
            anagram_dict[u.joined_sorted_lex()] = []  # adding to the dictionary keys
    return anagram_dict


def find_similar_for_values(diction, open_file):  # a method for looping the file again and finding the words that
    # share the same anagram for adding to the values/empty lists
    with open(open_file, encoding='utf8') as d:
        for y in d:
            q = y.strip()
            j = word_to_list(q)
            if j in diction.keys():
                diction[j].append(q)


def list_to_elements(list_in):  # a simple mwthod making elements of a list into a fine string of words
    return ', '.join(list_in)


def creating_game_data(filename):  # with adding the file we create the main data/dictionary used in program
    q = make_dict_keys(filename)
    find_similar_for_values(q, filename)
    return q


def menu(input_1, lexi_dict):  # the main menu for the program
    if input_1.lower() == 'ja':  # if the answer is only 'yes' case insensitive
        anv_inm = input('Skriv in ett valfritt svenskt ord: ')  # asking for input
        if anv_inm.isalpha() is False:  # reading from user input only if it is not a string
            print(f'"{anv_inm}" är troligtvis ett ogiltigt tecken')
            next_round_input = input('Vill du prova ett annat ord: ')
            menu(next_round_input, lexi_dict)
        else:  # reading from user input if it is a string
            if word_to_list(anv_inm) not in lexi_dict.keys():  # if the user input is not in the dictionary
                print(f'"{anv_inm}" finns inte i just den här ordlistan')
                next_round_input = input('Vill du prova ett annat ord: ')
                menu(next_round_input, lexi_dict)
            else:  # if it is in the dictionary
                if len(lexi_dict[word_to_list(anv_inm)]) == 0:  # if there are no anagrams
                    print(f'Det finns inga anagram för "{anv_inm}"')
                    next_round_input = input('Vill du prova ett annat ord: ')
                    menu(next_round_input, lexi_dict)
                else:  # if there are anagrams
                    print(f'Det finns {len(lexi_dict[word_to_list(anv_inm)])} anagram för ditt ord:\n'
                          f'{list_to_elements(lexi_dict[word_to_list(anv_inm)])}\n')
                    next_round_input = input('Vill du prova ett annat ord: ')
                    menu(next_round_input, lexi_dict)

    elif input_1.lower() == 'nej':  # if the answer is 'no' (case insensitive)
        print('Tråkigt, men vi hoppas på ett återbesök :)\nHejdå så länge')
        sys.exit()

    else:  # if the answer is anything other than 'yes' or 'no' (both case insensitive
        new_input = input(f'Inte helt säkert vad du menar med "{input_1}",\nkan du vara mer tydlig!')

        menu(new_input, lexi_dict)  # going back to main menu


if __name__ == "__main__":

    print('Dags att spela ett kult ordspel\n\n-------------***Spelet laddas***------------- ')
    main_lexi_dict = creating_game_data('sv-utf8.txt')
    choice_2 = input('Vill du spela: ')

    menu(choice_2, main_lexi_dict)
