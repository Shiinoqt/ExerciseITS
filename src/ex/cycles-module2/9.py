# ex. 9
while True:
    n = int(input("Type divisore: "))
    if n > 0 and n % 1 == 0:
        cont = 0
        i = 1
        for i in range(10):
            x = int(input("Type number: "))
            if x % n == 0:
                cont += 1
        print(f"I numeri divisibili sono: {cont}")
    else:
        print("Il numero deve essere intero positivo")