def left_rotate_by_one(arr):
    n = len(arr)
    if n == 0:
        return arr
    return arr[1:] + [arr[0]]

arr = [1, 2, 3, 4, 5]
rotated = left_rotate_by_one(arr)
print("Rotated:", rotated)  # [2, 3, 4, 5, 1]


def left_rotate_by_one_inplace(arr):
    if not arr:
        return arr
    first = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[-1] = first
    return arr

arr = [1, 2, 3, 4, 5]
left_rotate_by_one_inplace(arr)
print("Rotated:", arr)  # [2, 3, 4, 5, 1]

