def find_single_brute(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) +1

    for key, value in freq.items():
        if value == 1:
            return key


def find_single_optimal(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

print(find_single_brute([2, 2, 1]))        # Output: 1
print(find_single_brute([4, 1, 2, 1, 2]))  # Output: 4
