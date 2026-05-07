# def left_rotate_by_k(arr, k):
#     n = len(arr)
#     if n == 0:
#         return arr
#     return arr[k:] + arr[:k]
#
# arr = [1, 2, 3, 4, 5]
# k = 2;
# rotated = left_rotate_by_k(arr , k)
# print("Rotated:", rotated)  # [2, 3, 4, 5, 1]

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate_by_k(arr, k):
    n = len(arr)
    if n == 0:
        return arr

    k = k % n  # Handle k > n

    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)

    return arr


arr = [3, 7, 8, 9, 10, 11]
k = 3
print("Original Array : ", arr)
left_rotate_by_k(arr, k)

print("Left Rotated:", arr)  # [9, 10, 11, 3, 7, 8]

