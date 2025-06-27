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


def printMAT(mat: list[list[int]]) -> None:

    for r in range(len(mat)):

        for c in range(len(mat[r])):
            print(f"{mat[r][c]:<5}", end="")

        print("\n")


if __name__ == "__main__":

    mat = genera(4)
    printMAT(mat)