
def is_armstrong_brute(n):
    digits = str(n)
    len_digit = len(digits)

    total = 0
    for digit in digits:
        total += int(digit) ** len_digit

    return  total == n

print(is_armstrong_brute(153))  # True
print(is_armstrong_brute(12))   # False