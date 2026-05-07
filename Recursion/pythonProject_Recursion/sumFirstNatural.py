def sumOfNatural(N):
    if N <= 0:
        return N
    return sumOfNatural(N-1) + N

output = sumOfNatural(2)
print(output)