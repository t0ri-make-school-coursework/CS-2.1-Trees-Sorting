#!python
from sorting_iterative import insertion_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n) to go through each index
    Memory usage: O(n) to create new n-sized array"""
    merged = list()
    
    while len(items1) > 0 and len(items2) > 0:
        if items1[0] > items2[0]:
            merged.append(items2[0])
            items2.pop(0)
        elif items1[0] <= items2[0]:
            merged.append(items1[0])
            items1.pop(0)

    merged.extend(items1)
    merged.extend(items2)

    return merged


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time: O(n^2) always, to sort and merge
    Memory usage: O(n) to create new list (merged)"""
    items1 = insertion_sort(items[:len(items) // 2])
    items2 = insertion_sort(items[len(items) // 2:])
    
    merged = merge(items1, items2)

    items[:] = merged

    return items


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n log n), work is divided by 2 each time
    Memory usage: O(n) to store items"""
    length = len(items)
    if length is 1:
        return items
    
    items1 = merge_sort(items[:length // 2])
    items2 = merge_sort(items[length // 2:])
    items[:] = merge(items1, items2)

    return items

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
