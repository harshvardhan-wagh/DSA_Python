def union_of_arrays(arr1, arr2):
    return list(set(arr1).union(set(arr2)))

def union_sorted_arrays(arr1, arr2):
    i = j = 0
    union = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
        else:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union


print(union_sorted_arrays([1, 2, 3, 4, 5], [2, 3, 4, 4, 5]))
# [1, 2, 3, 4, 5]

print(union_sorted_arrays(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [2, 3, 4, 4, 5, 11, 12]
))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
