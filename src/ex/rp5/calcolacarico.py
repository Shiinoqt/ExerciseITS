def calcolaCarico(mat: list[list[int]], r: int, c: int):
    
    sommaRow = sum(mat[r])
    
    sommaCol = sum(mat[i][c] for i in range(len(mat)))

    carico = sommaRow + sommaCol - mat[r][c]

    return carico

if __name__ == "__main__":
    # Matrice di esempio
    matrice_esempio = [
        [1, 2, 3],
        [4, 5, 6,],
        [7, 8, 9]
    ]

    print(calcolaCarico(matrice_esempio, 1, 1))