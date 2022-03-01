"""making the bigram dictionary with distributive probability as values"""

from nltk import word_tokenize
from collections import defaultdict

bigram_freq_dict = defaultdict(int)


def make_dict(filename):  # method for reading from a training text file and making bigrams
    with open(filename, encoding='utf8') as f:
        for line in f:
            sent_1_try = line.lower()
            tokened_line = word_tokenize(sent_1_try)
            for i in range(len(tokened_line)-1):
                bigram_freq_dict[(tokened_line[i], tokened_line[i+1])] += 1

        return bigram_freq_dict
