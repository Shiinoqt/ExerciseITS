n = int(input("Type number: "))

somma = 0
i = 1

if n % 1 == 0:
    if n > 0 and n <= 100:
        while i < n:
            if i % 2 == 0:
                somma += i
            i += 1
        print(somma)
    elif n == 0 or n < 0:
        print("Error")
    else:
        while i < n:
            if i % 2 != 0:
                somma += i
            i += 1
        print(somma)
            
