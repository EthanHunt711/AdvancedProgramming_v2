def binary_search(l_sorted, target_x):
    """This function takes two parameters: a sorted list
    and a target value"""
    try:
        assert l_sorted == sorted(l_sorted)  # check if the list is sorted which is a requirement
    except AssertionError:
        print('The input list is not sorted')  # handling the unsorted list error
    else:
        n = len(l_sorted)
        left = 0  # the left bound
        right = n-1  # the right bound
        if right >= left:
            middle = (left + right) // 2  # dividing the list for a quicker search
            if target_x == l_sorted[middle]:  # if the target is the middle item
                return True
            elif target_x > l_sorted[middle]:  # if the target value is in the right half
                left = middle+1  # alter the left bound
                return binary_search(l_sorted[middle+1:], target_x)
            else:  # if the target value is in the left half
                right = middle-1  # alter the right bound
                return binary_search(l_sorted[:middle], target_x)
        return False   # if the target value is not in the list
