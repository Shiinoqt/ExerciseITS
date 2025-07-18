from calcolacarico import calcolaCarico

def caricoMax(mat: list[list[int]]) -> tuple[int, int]:
    max_carico = float('-inf')
    posizione_max = (0, 0)

    for r in range(len(mat)):
        for c in range(len(mat[r])):
            carico = calcolaCarico(mat, r, c)
            if carico > max_carico:
                max_carico = carico
                posizione_max = (r, c)

    print(f"Carico massimo: {max_carico}")
    return posizione_max

if __name__ == "__main__":
    matrice = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrice2 = [
        [10, 1, 2],
        [3, 20, 4],
        [5, 6, 30]
    ]

    print(caricoMax(matrice)) 
    print(caricoMax(matrice2))  