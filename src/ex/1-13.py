a = int(input("Input 1: "))
b = int(input("Input 2: "))
c = int(input("Input 3: "))

if a < 0 or b < 0 or c < 0:
    print("Hai messo un numero negativo")
elif (a+b+c) % 2 == 0 and a % 2 == 0 and b % 5 == 0 and c % 7 == 0:
    print("Regole rispettate")
else: 
    print("Regole non rispettate")