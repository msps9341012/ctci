def rotate_matrix(mat):
	n=len(mat)
	rotm = [None] * n
	for row in range(n):
		rotm[row] = [None] * n
	for row in range(n):
		for col in range(n):
			rotm[col][n-row-1] = mat[row][col]
	return rotm



def rotate_matrix_inplace(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[n-i-1][layer]

            # bottom -> left
            matrix[n-i-1][layer] = matrix[n-layer-1][n-i - 1]

            # right -> bottom
            matrix[n-layer- 1][n-i-1] = matrix[i][n-layer- 1]

            # top -> right
            matrix[i][n-layer- 1] = top
    return matrix

data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]
print(rotate_matrix_inplace(data[0][0])==data[0][1])

