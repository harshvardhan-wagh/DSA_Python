
def is_prime_simple(n):
    if n <= 1:
        return False  # 0 and 1 are not prime
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_prime_simple(5))  # True
print(is_prime_simple(8))  # False
