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


def main(filename):
    q = make_dict_keys(filename)
    find_similar_for_values(q, filename)
    return q


if __name__ == "__main__":
    lexi_dict = main('sv-utf8.txt')
    anv_inm = input('Dags för ett kult ordspel\n\nSkriv in ett valfritt svenskt ord: ')
    while True:
        if type(anv_inm) != str:
            print(f'{anv_inm} är troligtvis ett ogiltigt tecken')
        else:
            if word_to_list(anv_inm) not in lexi_dict.keys():
                print(f'{anv_inm} finns inte i just den här ordlistan')
            else:
                if len(lexi_dict[word_to_list(anv_inm)]) == 0:
                    print(f'Det finns inga anagram för {anv_inm}')
                else:
                    print(f'alla ord i den här listan delar samma anagram som ordet inmatade:\n'
                          f'{lexi_dict[word_to_list(anv_inm)]}')

