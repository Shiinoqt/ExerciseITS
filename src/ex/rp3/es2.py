def validNumber(x: int) -> None:
    if isinstance(x, int) and x > 0:
        return True

status: bool = True

while status:
    x = int(input("Inserisci un numero 'x' intero positivo: "))
    numbers: list[int] = []
    numbersWithoutX: list[int] = []
    numbersDict: dict[int, int] = {}

    if validNumber(x):
        found_x = False
        pos_x = None
        while True:
            y = int(input("Inserisci numero: "))
            if validNumber(y) and y != 0:
                numbers.append(y)
                if y in numbersDict:
                    numbersDict[y] += 1
                else:
                    numbersDict[y] = 1
                if y != x:
                    numbersWithoutX.append(y)

                # Saving position of first occurrence of x
                if y == x:
                    pos_x = len(numbers) 
            else:
                status = False
                break

print(f"\nSequenza dei numeri inseriti: {', '.join(str(n) for n in numbers)}")
print(f"Il numero {x} è stato inserito {numbersDict[x]} volta/e.")
print(f"Il numero {x} compare per la prima volta in posizione {pos_x} nella sequenza.")
print(f"La somma dei numeri diversi da {x} è: {sum(numbersWithoutX)}.")