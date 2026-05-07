# Example usage

def second_smallest_largest_better(arr):
    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')

    for num in arr:
        # Smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num

        # Largest
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    if second_smallest == float('inf'):
        second_smallest = -1
    if second_largest == float('-inf'):
        second_largest = -1

    return second_smallest, second_largest


# Example usage
arr = [1, 2, 4, 7, 7, 5]
second_smallest, second_largest = second_smallest_largest_better(arr)
print("Second Smallest:", second_smallest)
print("Second Largest:", second_largest)


