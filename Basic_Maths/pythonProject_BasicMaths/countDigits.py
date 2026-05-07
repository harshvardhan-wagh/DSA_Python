# Normal Basic
# numbers = 1234
# digit_count =len(str(numbers))
# print(f"Total Digit : {digit_count}")

# Ideal
numbers = "1234"
digit_count = sum(1 for char in numbers if char.isdigit())
print(f"Digit Count : {digit_count}")