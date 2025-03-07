# ex. 8

a = int(input("Type number: "))
b = int(input("Type number: "))

if a < b:
    if a > 0 and b > 0:
        if a % 1 == 0 and b % 1 == 0:
            somma = 0
            i = a
            while i <= b:
                somma += i
                i += 1
            print(somma)
        else:
            print("A e B devono essere interi")
    else:
        print("A e B devono essere positivi")
else:
    print("A deve essere minore di B")



if a < b:
    if a > 0 and b > 0:
        if a % 1 == 0 and b % 1 == 0:
            somma = 0
            i = a
            while i <= b:
                somma += i
                i += 1
            print(somma)
        else:
            print("A e B devono essere interi")
    else:
        print("A e B devono essere positivi")
else:
    print("A deve essere minore di B")