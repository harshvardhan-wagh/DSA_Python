height = 5
width = 5

for i in range(1, height+1):
    left = "".join(str(j) for j in range(1,i+1))
    space = " " * (2 * (width - i) )
    right = "".join(str(j) for j in range(i ,0 , -1))

    print(left + space +right)




