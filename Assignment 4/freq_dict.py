import re
from nltk import sent_tokenize, word_tokenize

from collections import defaultdict

freq_dict = defaultdict(int)


def make_list(filename):
    with open(filename, encoding='utf8') as f:
        list_of_bigrams = []
        for line in f:
            sent = line.split()
            for i, word in enumerate(sent):
                if i == 0:
                    list_of_bigrams.append(('<s>', sent[i].lower()))

                elif i == len(sent)-1:
                    list_of_bigrams.append((sent[i].lower(), '<e>'))

                elif 0 < i < len(sent)-1:
                    list_of_bigrams.append((sent[i].lower(), sent[i+1].lower()))
        return list_of_bigrams


def make_dict(filename):
    list_of_b = make_list(filename)
    for bi_gram in list_of_b:
        if bi_gram not in freq_dict:
            freq_dict[bi_gram] = 0
        freq_dict[bi_gram] += 1
    return freq_dict
