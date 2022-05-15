def absDiffDiagonal(matrix):
    integer = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                var = len(matrix[0]) - 1 - j
                integer = integer + (matrix[i][i] - matrix[i][var]) 

    
    if integer < 0:
        return integer * (-1)
    else:
        return integer
                
                
print(absDiffDiagonal([[1,2,3],[4,5,6],[9,8,9]]))