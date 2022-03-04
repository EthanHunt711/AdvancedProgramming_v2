from random import randint
"""The lists are identical in size and range of the numbers but since the numbers are randomly 
selected it is possible that the target value might appear in one and not the other(s)"""


def get_random(r_s, r_e):
    list_of_random_numbers = []
    for i in range(r_s, r_e):
        rand_n = randint(1, 10000000)
        list_of_random_numbers.append(rand_n)
    return list_of_random_numbers
