from Linear_search import linear_search
from Binary_search import binary_search
from Bubble_sort import bubble_sort

from get_random import *
import time


def main(random_lists, list_index=0):
    # the running time for the linear search
    something_start = time.time()
    something_l = linear_search(random_lists, list_index)
    something_stop = time.time()
    something_running_time_linear = something_stop - something_start

    # the running time for the binary search
    something_start = time.time()
    something_b = binary_search(sorted(random_lists), list_index)
    something_stop = time.time()
    something_running_time_binary = something_stop - something_start

    # the running time for the bubble sort
    something_start = time.time()
    something_bl = bubble_sort(random_lists)
    something_stop = time.time()
    something_running_time_bubble = something_stop - something_start

    print(f'The running time for Linear Search is: {something_running_time_linear}')
    print(f'The serach result is: {something_l}')
    print('---------------------------------------------------------------------------')
    print(f'The running time for Binary Search is: {something_running_time_binary}')
    print(f'The search result is: {something_b}')


"""The main program for implementing the algorithms. The running time
could be saved in a .csv file if it is run in the terminal"""

if __name__ == "__main__":
    lists = []
    for i in range(10):
        lists.append(get_random(0, 994))  # maximum recursion is 994
    n = 0
    for lists_w in lists:  # looping through the lists since the data is a list of random lists
        print(f'Search reults for list {n+1} with {len(lists_w)} elements')
        main(lists_w, n)
        print('---------------------------------------')
        print('---------------------------------------')
        n += 1
