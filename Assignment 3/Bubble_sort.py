def bubble_sort(this_list):
    """This function takes an unsorted list as input and returns the list sorted."""
    swap = True  # use bool to keep track of whether swaps were made
    for i in range(len(this_list)-1):  # compare each pair of adjacent items
        if this_list[i] > this_list[i+1]:  # check if the first item is bigger
            this_list[i], this_list[i+1] = this_list[i+1], this_list[i]  # swap the two items
            swap = False  # change the bool
    if swap:  # if no swaps were made
        return this_list  # return the list
    return bubble_sort(this_list)  # sort again
