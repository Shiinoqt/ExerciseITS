def sum_primary_diagonal(matrix):
    sumDiag = 0
    for i in range(len(matrix)):
        sumDiag += matrix[i][i]

    return sumDiag
    
def sum_secondary_diagonal(matrix):
    sumDiag = 0
    n = len(matrix)
    for i in range(n):
        sumDiag += matrix[i][n - 1 - i]

    return sumDiag

mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
print(sum_primary_diagonal(mat1)) # restituisce 1 + 5 + 9 = 15
print(sum_secondary_diagonal(mat1)) # restituisce 3 + 5 + 7 = 15