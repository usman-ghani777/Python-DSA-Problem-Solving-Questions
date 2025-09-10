nums = [[5,20,9],[7,-10,9],[1,-52,6]]
rows = len(nums)
cols = len(nums[0])

result = [[0]*rows for _ in range(0,cols)]
for i in range(0,rows):
    for  j in range(0,cols):
        result[j][i] = nums[i][j]
    print(result)