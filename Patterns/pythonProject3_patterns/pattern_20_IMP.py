
height = 5
width = 5

for i in range(1, height+1):
    left = "".join(str('*') for j in range(1, i +1))
    middle= " " * (2 * (width - i))
    right = "".join(str("*") for j in range(i , 0 , -1))


    print((left + middle + right))

for i in range(height, 0, -1):
    left = "".join(str("*") for j in range(1, i + 1))
    middle = " " * (2 * (height - i))
    right = "".join(str("*") for j in range(i, 0, -1))
    print(left + middle + right)
