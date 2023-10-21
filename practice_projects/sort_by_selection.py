#! python3

"""Sorting by Selection

This program implements a sort by selection algorithm and returns a list in ascending order.

How to use:
Inside the file create a list and pass it as a parameter to the sort_by_selection() function, then print the output of the function. 
Ex:
    print(sort_by_selection([2, 4, 10, 3, 5, 9, 8, 7]))

Execution:
    python3 sort_by_selection.py
"""

def minor_search(arr):
    """
    Finds the smallest index in a list.

    return: smallest index in the list.
    """
    minor = arr[0]
    minor_indx = 0
    for i in range(1, len(arr)):
        if arr[i] < minor:
            minor = arr[i]
            minor_indx = i
    return minor_indx


def sort_by_selection(arr):
    """
    Sorts a list by selecting a value.
    Uses the function minor_search() to find the smallest value in the list and sort the list in ascending order.

    return: A new list in ascending order.
    """
    new_arr = []
    for _ in range(len(arr)):
        minor = minor_search(arr)
        new_arr.append(arr.pop(minor))
    return new_arr

print(sort_by_selection([2, 4, 10, 3, 5, 9, 8, 7]))
