def transpose(given_matrix):
    row = len(given_matrix)
    column = len(given_matrix[0])
    matrix = []
    for i in range(column):
        matrix.append([])
    for element in matrix:
        for j in range(row):
            element.append(0)
    
    for i in range(len(given_matrix)):
        for j in range(len(given_matrix[0])):
            matrix[j][i] = matrix[i][j]
    
    return matrix
   

transpose([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10,11, 12]])
    
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
            