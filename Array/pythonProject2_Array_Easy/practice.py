def find_second_largest(arr):
    largest = second_largest = float('-inf')

    for num in arr[1:]:
        if num > largest:
            largest = num
        if num > second_largest and num < largest:
            second_largest = num


    return second_largest



arr1 = [2, 5, 1, 3, 0]
# arr2 = [8, 10, 5, 7, 9]
#
print("Largest Element : ",find_second_largest(arr1))


