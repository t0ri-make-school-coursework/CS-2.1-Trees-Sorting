#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) worst case (True), O(1) best case (False)
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i, item in enumerate(items):
        if i is not len(items) - 1: # Check if item is last index in array
            if item > items[i + 1]:
                return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n) best case, has to check if in sorted order
    TODO: Memory usage: ??? Why and under what conditions?"""
    if len(items) is 0:
        return items
    
    unsorted = True
    while unsorted:
        for i, item in enumerate(items):
            if i is not len(items) - 1: # Check if item is last index in array
                if item > items[i + 1]:
                    items[i], items[i + 1] = items[i + 1], items[i]
            elif is_sorted(items): # Only check if in sorted order at end of array
                unsorted = False
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) worst cacse, double loop through all indeces
    O(n) if list is already sorted
    TODO: Memory usage: ??? Why and under what conditions?"""
    if is_sorted(items):
        return items

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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
