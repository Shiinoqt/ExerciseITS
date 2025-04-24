def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    risultato = {}

    for voto in voti:
        nome = voto['nome']
        
        if nome not in risultato:
            risultato[nome] = []

        risultato[nome].append(voto['voto'])

    return risultato





print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))