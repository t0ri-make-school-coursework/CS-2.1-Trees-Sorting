#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(range + n) because the amount of passes in loops depends
    n and the maximum value that we use to init the histogram
    TODO: Memory usage: ??? Why and under what conditions?"""
    if numbers:
        # Find range of given numbers (minimum and maximum integer values)
        maximum = max(numbers) # O(n)
        minimum = min(numbers) # O(n)
        
        # Create list of counts with a slot for each number in input range
        histogram = [0 for _ in range(maximum - minimum + 1)] # O(max)
        
        # Loop over given numbers and increment each number's count
        for number in numbers: # O(n)
            histogram[number - minimum] += 1 # O(1)
        
        # Loop over counts and append that many numbers into output list
        pointer = 0
        for index, item in enumerate(histogram):
            for _ in range(0, item): # item is frequency
                numbers[pointer] = index + minimum # O(n)
                pointer += 1
        
    return numbers


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n log n)
    TODO: Memory usage: ??? Why and under what conditions?"""
    if numbers:
        # Find range of given numbers (minimum and maximum values)
        maximum = max(numbers) # O(n)
        minimum = min(numbers) # O(n)
        
        # Create list of buckets to store numbers in subranges of input range
        buckets = [[] for _ in range(num_buckets)]
        
        # Loop over given numbers and place each item in appropriate bucket
        for number in numbers:
            bucket_index = (number * num_buckets) // (maximum + 1)
            buckets[bucket_index].append(number)
        
        number_index = 0
        # Loop over buckets and append each bucket's numbers into output list
        for bucket in buckets:
            # Sort each bucket using any sorting algorithm
            bucket.sort()
            for number in bucket:
                numbers[number_index] = number
                number_index += 1
    
    return numbers
