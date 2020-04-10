#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) worst case if returns True
    Memory usage: O(1) """
    for i, item in enumerate(items):
        if i is not len(items) - 1: # Check if item is last index in array
            if item > items[i + 1]:
                return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2) worst case, nested for loop
    Memory usage: O(1) no new vars"""
    if len(items) is 0:
        return items
    
    for i in range(len(items)):
        for j in range(len(items) - i - 1): # Remove looping items in place
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) avg case, double loop through all indeces
    Memory usage: O(1) 1 var (minimum), swaps in place"""
    for swaps in range(len(items) - 1):
        minimum = items[swaps], swaps

        for i, item in enumerate(items[swaps:]):
            if item <= minimum[0]:
                minimum = item, i + swaps
        
        items[minimum[1]], items[swaps] = items[swaps], items[minimum[1]]
    
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n) best case, one loop of all items
    O(n^2) worst case, if lots of swaps cause index to decrease
    Memory usage: O(1) 1 var reused"""
    for index in range(1, len(items)):
        value = items[index]
        while index > 0 and items[index - 1] > value:
            items[index] = items[index - 1]
            index -= 1 # same index again

        items[index] = value

    return items
