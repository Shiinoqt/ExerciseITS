from calcolacarico import calcolaCarico

def caricoNullo(mat: list[list[int]]) -> list[tuple[int, int]]:
    posizioniNulle = []
    
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            carico = calcolaCarico(mat, r, c)
            if carico == 0:
                posizioniNulle.append((r, c))
    
    return posizioniNulle

if __name__ == "__main__":
    # Matrice di esempio
    matrice_esempio = [
        [1, 0, 3],
        [0, 0, 0],
        [0, 8, 9]
    ]

    matrice_esempio2 = [
        [1, -1, 0],
        [0,  0, 0],
        [-1, 1, 0]
    ]

    print(caricoNullo(matrice_esempio))
    print(caricoNullo(matrice_esempio2))