def filtra_moltiplica(lista_numeri: list[int], fattore: int) -> list[int]:
    results = []

    for i in lista_numeri:
        if i % 2 == 0:
            results.append(i * fattore)

    return results

print(filtra_moltiplica([1, 2, 3, 4, 5, 6], 3)) 
print(filtra_moltiplica([], 3))