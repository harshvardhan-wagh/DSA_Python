
def natural_number(n):
    if n <= 0:
        return n
    return natural_number(n-1) + n

print(natural_number(2))