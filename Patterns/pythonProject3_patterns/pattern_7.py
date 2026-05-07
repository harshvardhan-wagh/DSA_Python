height = 5;
width = 5;

for i in range( 1 ,height + 1 ):
    space= ' '* (width - i)
    stars = '*' * ( 2 * i -1)

    print(space + stars)

