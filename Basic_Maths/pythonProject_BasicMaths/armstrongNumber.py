def is_armstrong_brute(n):
    # Convert the number to a string to count digits and extract digits
    digits = str(n)
    num_digits = len(digits)

    # Calculate the sum of each digit raised to the power of num_digits
    total = 0
    for digit in digits:
        total += int(digit) ** num_digits

    # Compare the total with the original number
    return total == n



print(is_armstrong_brute(153))  # True
print(is_armstrong_brute(12))   # False
