def move_zeros_to_end_extra_space(arr):

    arr_num = []
    for num in arr:
        if num != 0:
            arr_num.append(num)

    arr_num.extend([0] *(len(arr)-len(arr_num)))

    return arr_num










arr = [1, 0, 2, 3, 0, 4, 0, 1]
print(move_zeros_to_end_extra_space(arr))  # [1, 2, 3, 4, 1, 0, 0, 0]