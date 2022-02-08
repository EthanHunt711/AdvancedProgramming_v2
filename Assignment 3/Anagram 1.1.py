from collections import defaultdict
from Bubble_sort import bubble_sort


anagram_dict = defaultdict(lambda: 'Ordet hittades inte')


def add_to_dict(filename):  # creating the dictionary
    with open(filename, encoding='utf8') as in_f:
        for word in in_f:
            word = word.strip()
            anagram_dict[bubble_sort(list(word))] = bubble_sort(list(word))

def find_same_letters(word):
    for letter in word:
        pass
class Anagram:
    def __init__(self, lexicon):
        self.lexicon = lexicon


def main():
    anv_inmat = input('Skriv ett valfritt ord: ')

    pass


# if __name__ == "__main__":
#     main()