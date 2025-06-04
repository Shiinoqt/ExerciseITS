def converter(tuples: list[tuple]) -> dict:

    dizionario = {}

    for tupla in tuples:
        chiave, valore = tupla

        if chiave not in dizionario:
            dizionario[chiave] = []
            
        dizionario[chiave].append(valore)

    return dizionario


print(converter([("a", 1), ("b", 2), ("a", 2)]))