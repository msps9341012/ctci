
def zeromatrix(mat):
	rows=[] #如果不記位置 ˋ整個matrix會變零
	cols=[]
	row_length=len(mat)
	column_length=len(mat[0])
	for i in range(row_length):
		for j in range(column_length):
			if mat[i][j]==0:
				rows.append(i)
				cols.append(j)
	
	for row in rows:
		nullify_row(mat, row)
	for col in cols:
		nullify_col(mat, col)
	return mat


def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

print(zeromatrix(data[0][0])==data[0][1])
