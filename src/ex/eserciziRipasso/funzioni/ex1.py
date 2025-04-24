def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    dizionario = {}

    for tupla in tuples:
        chiave, valore = tupla

        if chiave not in dizionario:
            dizionario[chiave] = []
            
        dizionario[chiave].append(valore)

    return dizionario


print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))
print(lista_a_dizionario([]))