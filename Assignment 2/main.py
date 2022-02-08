from binary_search import binary_search
from linear_search import linear_search
from bubble_sort import bubble_sort

from get_random import lists
import time


def main(random_lists, list_index=0):
    # the running time for the linear search
    something_start = time.time()
    something_l = linear_search(random_lists[list_index], 5)
    something_stop = time.time()
    something_running_time_linear = something_stop - something_start

    # the running time for the binary search
    something_start = time.time()
    something_b = binary_search(sorted(random_lists[list_index]), 5)
    something_stop = time.time()
    something_running_time_binary = something_stop - something_start

    # the running time for the bubble sort
    something_start = time.time()
    something_bl = bubble_sort(random_lists[list_index])
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
    n = 0
    for list in lists:  # looping through the lists since the data is a list of random lists
        print(f'Search reults for list {n+1} with {len(list)} elements')
        main(lists, n)
        print('---------------------------------------')
        print('---------------------------------------')
        n += 1
