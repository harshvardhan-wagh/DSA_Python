# BruteForce
# num = 1234321
# reversed_num = str(num)[::-1]
# print(f"reverse: {reversed_num}")
#
# if str(num) == reversed_num:
#     print("Is Palindrome")
# else:
#     print("Not Palindrome")


def is_palindrome_optimized(N):
    original = N
    reverse_num = 0

    # Reverse the number mathematically
    while N > 0:
        digit = N % 10  # Get last digit
        reverse_num = reverse_num * 10 + digit  # Build reversed number
        N //= 10  # Remove last digit

    # Compare reversed number with original
    return "Palindrome Number" if original == reverse_num else "Not Palindrome"


# Example cases
print(is_palindrome_optimized(4554))  # Output: Palindrome Number
print(is_palindrome_optimized(7789))  # Output: Not Palindrome
