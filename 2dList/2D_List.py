# nums = [[5,20,9],[7,-10,9],[1,-52,6]]
# rows = len(nums)
# cols = len(nums[0])
# for i in range(0,rows):
#     for  j in range(0,cols):
#         print(nums[i][j],end=" ")
#     print()

#**********************************************
nums = [[5,20,9],[7,-10,9],[1,-52,6]]
rows = len(nums)
cols = len(nums[0])
for i in range(0,rows):
    for  j in range(0,cols):
        if j==i:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()