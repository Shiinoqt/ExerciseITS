from calcolacarico import calcolaCarico

def caricoMin(mat: list[list[int]]) -> tuple[int, int]:
    min_carico = float('inf')
    posizione_min = (0, 0)

    for r in range(len(mat)):
        for c in range(len(mat[r])):
            carico = calcolaCarico(mat, r, c)
            if carico < min_carico:
                min_carico = carico
                posizione_min = (r, c)

    print(f"Carico minimo: {min_carico}")
    return posizione_min
