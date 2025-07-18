from random import randint

def genera(n: int) -> list[list[int]]:
    mat = []
    for r in range(n):
        row = []

        for c in range(n):
            # Riempie la prima colonna con n random da 0,13
            if c == 0:
                number = randint(0,13)
                row.append(number)

            # Riempie il resto della colonne
            else:

                # Entra in un loop in cui finchè il numero è diverso dal primo della riga lo aggiunge
                while True:
                    number = randint(0, 13)
                    if number != row[0]:
                        row.append(number)
                        break

        mat.append(row)

    return mat
