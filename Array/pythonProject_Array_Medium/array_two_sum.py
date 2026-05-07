# def two_sum_brute(arr, target):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if arr[i] + arr[j] == target:
#                 return "YES", [i, j]  # Or return [i+1, j+1] if 1-based
#     return "NO", [-1, -1]
#
#
# arr = [2, 6, 5, 8, 11]
# print(two_sum_brute(arr, 14))  # ("YES", [1, 3])
# print(two_sum_brute(arr, 15))  # ("NO", [-1, -1])

def two_sum_optimal(arr, target):
    num_map ={}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_map:
            return "YES", [num_map[complement], i]
        num_map[num] = i
    return "NO", [-1, -1]

arr = [2, 6, 5, 8, 11]
print(two_sum_optimal(arr, 14))  # ("YES", [1, 3])
print(two_sum_optimal(arr, 15))  # ("NO", [-1, -1])
