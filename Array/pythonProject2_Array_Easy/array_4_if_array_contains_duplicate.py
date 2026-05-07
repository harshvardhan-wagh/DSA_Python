def remove_duplicates(arr):
    if not arr:
        return 0

    i = 0  # First unique element is always at index 0

    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1  # Length of unique portion



arr = [1, 1, 2, 2, 2, 3, 3]
k = remove_duplicates(arr)
print("Unique count:", k)
print("Modified array:", arr[:k], "+", arr[k:])  # Optional
