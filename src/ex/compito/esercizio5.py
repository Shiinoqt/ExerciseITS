chocolate = 0
discount = 6
total = 0
while True:
    cash = int(input("Insert cash: "))
    total += cash
    print(f"Hai comprato {total} barrette.")
    if total % discount == 0:
        chocolate += 1
        totalNew = total + chocolate
        print(f"Hai ricevuto {chocolate} barretta/e in piu! In totale sono: {totalNew}.")