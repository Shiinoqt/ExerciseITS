def classifica_numeri(lista: int) -> dict[str:list[int]]:
    dictN = {'pari':[], 'dispari':[]}
    for n in lista:
        if n%2==0:
            dictN['pari'].append(n)
        else:
            dictN['dispari'].append(n)
            
    return dictN

