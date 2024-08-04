#Better approach
def zeroMatrix(matrix, n, m):
    row = [0] * n  
    col = [0] * m  
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0

    return matrix
if __name__ == "__main__":
	matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
	n = len(matrix)
	m = len(matrix[0])
	ans = zeroMatrix(matrix, n, m)

	print("The Final matrix is:")
	for row in ans:
	    for ele in row:
	        print(ele, end=" ")
print()