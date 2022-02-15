import sys
from collections import defaultdict
from Bubble_sort import bubble_sort

"""This is a program for which the user can check for anagrams. The user enters the line in  
terminal which specifies a dictionary/file and an input word (in Swedish for the current purpose) and see if there are 
other words in the given dictionary that shares exactly the same characters as the user's"""
# OBS!!! little change from the assignment instruction. The file containing the original words
# is to be mentioned in the terminal so there is a possibility to use for any language


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


if __name__ == "__main__":

    if len(sys.argv) != 3:  # if the arguments for the terminal is out of bound
        print('usage: python anagram-1-2.py FILE WORD ')
        exit()
    else:
        file_in = sys.argv[1]  # the file for unpacking and creating dictionary
        word_in = sys.argv[2]  # the word to search for
        print('Loading file and searching ...')
        lexi_dict = creating_game_data(file_in)
        if word_to_list(word_in) in lexi_dict.keys():
            print(f'{list_to_elements(lexi_dict[word_to_list(word_in)])}')
        else:
            print('')
