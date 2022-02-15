import sys
from collections import defaultdict
from Bubble_sort import bubble_sort


class LexicalEntry:
    def __init__(self, lex):
        self.lex = lex

    def split_lex(self):
        split_list = []
        for le in self.lex:
            split_list.extend(le.lower())
        return split_list

    def joined_sorted_lex(self):
        s = self.split_lex()
        j_lex = bubble_sort(s)
        s_lex = ''.join(j_lex)
        return s_lex


def word_to_list(word):
    w_l = []
    for el in word:
        w_l.append(el)
    return ''.join(bubble_sort(w_l))


def make_dict_keys(opened_file):  # creating the dictionary
    anagram_dict = defaultdict(list)
    with open(opened_file, encoding='utf8') as s:
        for lex_entry_line in s:
            w = lex_entry_line.strip()
            u = LexicalEntry(w)
            anagram_dict[u.joined_sorted_lex()] = []
    return anagram_dict


def find_similar_for_values(diction, open_file):
    with open(open_file, encoding='utf8') as d:
        for y in d:
            q = y.strip()
            j = word_to_list(q)
            if j in diction.keys():
                diction[j].append(q)

def list_to_elements(list_in):
    return ', '.join(list_in)

def creating_game_data(filename):
    q = make_dict_keys(filename)
    find_similar_for_values(q, filename)
    return q

def menu(input_1, lexi_dict):
    if input_1.lower() == 'ja':
        anv_inm = input('Skriv in ett valfritt svenskt ord: ')
        if type(anv_inm) != str:
            print(f'{anv_inm} är troligtvis ett ogiltigt tecken')
        else:
            if word_to_list(anv_inm) not in lexi_dict.keys():
                print(f'{anv_inm} finns inte i just den här ordlistan')
            else:
                if len(lexi_dict[word_to_list(anv_inm)]) == 0:
                    print(f'Det finns inga anagram för {anv_inm}')
                else:
                    print(f'Det finns {len(lexi_dict[word_to_list(anv_inm)])} anagram för ditt ord:\n'
                          f'{list_to_elements(lexi_dict[word_to_list(anv_inm)])}\n')
                    next_round_input = input('Vill du prova ett annat ord: ')
                    menu(next_round_input, lexi_dict)

    elif input_1.lower() != 'nej':
        new_input = input(f'Inte helt säkert vad du menar med "{input_1}",\nkan du vara mer tydlig!')

        menu(new_input, lexi_dict)

    else:
        print('Tråkigt, men vi hoppas på ett återbesök :)\nHejdå så länge')

        sys.exit()


if __name__ == "__main__":

    print('Dags att spela ett kult ordspel\n\n-------------***Spelet laddas***------------- ')
    main_lexi_dict = creating_game_data('sv-utf8.txt')
    choice_2 = input('Vill du spela: ')

    menu(choice_2, main_lexi_dict)
