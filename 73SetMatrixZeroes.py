def setZeroes(matrix):
    lin, col = False, False
        
    if 0 in matrix[0]:
        lin = True

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            col = True
            break

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    if lin:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0
    if col:
        for i in range(len(matrix)):
            matrix[i][0] = 0            

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)
print(matrix)
matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
print(matrix)
