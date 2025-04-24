def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    key = list(da_rimuovere.keys())
    value = list(da_rimuovere.values())

    x = key[0]
    y = value[0]
    
    for i in lista:
        if y > 0:
            if i == x:
                lista.remove(i)
                y -= 1
    
    return lista

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
print(rimuovi_elementi([], {2: 1})) 