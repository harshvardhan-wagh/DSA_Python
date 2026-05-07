# Example usage


# def find_largest(arr):
#     return max(arr)

def find_largest(arr):
    largest = arr[0]

    for num in arr[1:]:
        if num > largest:
            largest = num

    return  largest



arr1 = [2, 5, 1, 3, 0]
arr2 = [8, 10, 5, 7, 9]

print("Largest Element : ",find_largest(arr1))
