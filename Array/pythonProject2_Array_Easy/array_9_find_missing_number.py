def find_missing_brute(arr, N):
    for i in range(1, N + 1):
        if i not in arr:
            return i

def find_missing_number(arr, N):
    expected_sum = N * (N + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

def find_missing_xor(arr, N):
    xor_total = 0
    xor_array = 0

    for i in range(1, N + 1):
        xor_total ^= i

    for num in arr:
        xor_array ^= num

    return xor_total ^ xor_array


print(find_missing_number([1, 2, 4, 5], 5))  # Output: 3
print(find_missing_number([1, 3], 3))        # Output: 2


print(find_missing_xor([1, 2, 4, 5], 5))  # Output: 3
print(find_missing_xor([1, 3], 3))        # Output: 2


print(find_missing_brute([1, 2, 4, 5], 5))  # Output: 3
