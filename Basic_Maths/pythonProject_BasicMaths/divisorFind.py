def find_divisors_simple(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


print(find_divisors_simple(12))  # [1, 2, 3, 4, 6, 12]
