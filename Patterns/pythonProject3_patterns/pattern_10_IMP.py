height = 5

# Top half
for i in range(1, height + 1):
    stars = "*" * i
    print(stars)

# Bottom half
for i in range(height - 1, 0, -1):
    stars = "*" * i
    print(stars)
