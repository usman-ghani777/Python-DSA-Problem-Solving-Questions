# def mark_infinity(matrix, row, colm):
#     r = len(matrix)
#     c = len(matrix[0])
#     # Mark the whole column
#     for i in range(r):
#         if matrix[i][colm] != 0:
#             matrix[i][colm] = float('inf')
#     # Mark the whole row
#     for j in range(c):
#         if matrix[row][j] != 0:
#             matrix[row][j] = float('inf')

# def setzeros(matrix):
#     r = len(matrix)
#     c = len(matrix[0])
#     # First pass - mark
#     for i in range(r):
#         for j in range(c):
#             if matrix[i][j] == 0:
#                 mark_infinity(matrix, i, j)
#     # Second pass - set to zero
#     for i in range(r):
#         for j in range(c):
#             if matrix[i][j] == float('inf'):
#                 matrix[i][j] = 0

# matrix = [[1, 2, 1], [9, 0, 2], [7, 0, 9]]
# setzeros(matrix)
# print(matrix)
#***************************************************************************

matrix = [[1, 2, 1], [9, 0, 2], [7, 0, 9]]
r = len(matrix)
c = len(matrix[0])

row_track = [0 for _ in range(r)]
colm_track = [0 for _ in range(c)]

for i in range(r):
    for j in range(c):
        if matrix[i][j]==0:
            row_track[i] = -1
            colm_track[j] = -1
for i in range(r):
    for j in range(c):
        if row_track[i]==-1 or colm_track[j]==-1:
            matrix[i][j]=0
print(matrix)