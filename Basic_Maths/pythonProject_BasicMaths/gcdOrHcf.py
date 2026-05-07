# def gcd_brute_force(N1, N2):
#     common_factors = []
#
#     print(min(N1, N2) + 1)
#     # Find common factors
#     for i in range(1, min(N1, N2) + 1):
#         if N1 % i == 0 and N2 % i == 0:  # If 'i' is a factor of both
#             common_factors.append(i)
#
#     return max(common_factors)  # Return the greatest common factor
#
#
# # Example cases
# print(gcd_brute_force(9, 12))  # Output: 3
# print(gcd_brute_force(20, 15))  # Output: 5



# def gcd_euclidean_recursive(N1, N2):
#     if N2 == 0:
#         return N1  # Base case: GCD found
#     return gcd_euclidean_recursive(N2, N1 % N2)  # Recursive call
#
# # Example cases
# print(gcd_euclidean_recursive(9, 12))  # Output: 3
# print(gcd_euclidean_recursive(20, 15)) # Output: 5
#
#l
# def gcd_euclidean_iterative(N1, N2):
#     while N2:
#         N1, N2 = N2, N1 % N2  # Swap N1 with N2, and N2 with N1 % N2
#     return N1
#
# # Example cases
# print(gcd_euclidean_iterative(9, 12))  # Output: 3
# print(gcd_euclidean_iterative(20, 15)) # Output: 5
