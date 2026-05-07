height = 5;
width = 5;

# for i in range( height , 0 ,-1):
#     for j in range(1, i+1):
#         print(i , end="")
#     print()

for i in range(height , 0 ,-1):
    print("".join(str(j) for j in range (1  , i+1)))