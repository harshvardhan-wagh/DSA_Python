height = 5;
width = 5;

for i in range(1 ,height +1 ):

    left   = "".join(str(num) for num in range (1, i + 1))

    middle = " " * (2 * (height - i))

    right  = "".join(str(num) for num in range ( i , 0,-1))

    print(left + middle + right)

