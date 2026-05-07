def major_element(nums, n):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    target = n // 2
    for key, value in freq.items():
        if value > target:
            return key

def major_element_optimal(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate


print(major_element_optimal([3, 2, 3]))               # Output: 3
print(major_element_optimal([2, 2, 1, 1, 1, 2, 2]))   # Output: 2
print(major_element_optimal([4,4,2,4,3,4,4,3,2,4]))   # Output: 4
