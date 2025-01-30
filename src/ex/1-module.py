# # ex.1 
# import math
# a = int(input("Insert number: "))
# b = int(input("Insert number: "))

# if a > b:
#     c = math.sqrt(a**2 + b**2)
#     print(f"The square is: {c}")
# else:
#     print("Error")


# # ex.2
# max:int = 0
# i:int = 0
# while i < 4:
#     n = int(input("Insert number: "))
#     if n > max:
#         max = n
#     i += 1
# print(f"The max number is: {max}")

# # ex.3
# sum: int = 0
# i: int = 0
# while i < 5:
#     n = int(input("Insert number: "))
#     if n > 0:
#         sum += n
#     i += 1
# print(f"The sum is: {sum}")

# # ex.4 
# n = int(input("Insert number: "))
# if n % 2 == 0:
#     print("Il numero è pari.")
# else:
#     print("Il numero è dispari.")

# # ex.5
# import math
# primo : bool = True
# n = int(input("Insert number: "))
# if n < 2:
#     print("Il numero non è primo")
# else:
#     div = 2
#     while div <= math.sqrt(n):
#         if n % div == 0:
#             print("Il numero non è primo")
#             primo : bool = False
#             break
#         else:
#             div += 1
# if primo :            
#     print("Il numero è primo")

# # ex.6
# n = int(input("Insert number: "))
# if n > 0:
#     fat: int = 1
#     i = 1
#     while i <= n:
#         fat = fat * i
#         i += 1
#     print(fat)
# else:
#     print("Il numero deve essere positivo.")

# # ex.7
# i = 1
# pari : int = 0
# dispari : int = 0
# while i <= 10:
#     n: int = (int(input("Inserisci numero: ")))
#     if n % 2 == 0:
#         pari += 1
#     else:
#         dispari += 1
#     i += 1
# print(f"I numeri dispari sono: {dispari}, I numeri pari sono: {pari}")

# # ex.8
# soglia = int(input("Insert soglia: "))
# i = 0
# while i < 8:
#     n = int(input("Insert number: "))
#     if n > soglia:
#         print(f"{n} supera la soglia")
#     i += 1
    
# # ex. 9
# name = str(input("Inserisci nome venditore: "))
# vendite = int(input("INserisci numero vendite: "))

# maxName = name
# maxSales = vendite

# minName = name 
# minSales = vendite

# i = 0

# while i <= 20:
#     newName = str(input("Inserisci nome venditore: "))
#     newSales = int(input("INserisci numero vendite: "))
#     if newSales > maxSales:
#         maxName = newName
#         maxSales = newSales
#     elif newSales > minSales:
#         minName = newName
#         minSales = newSales
#     i += 1
# print(f"Il venditore con più vendite è: {maxName}, {maxSales} ed il venditore con meno vendite è: {minName}, {minSales}")


# # ex.10
# r = int(input("Inserisci reddito: "))
# m = int(input("Inserisci media voti: "))

# if r < 20000 and m > 27:
#     print("Borsa di studio approvata.")
# else: 
#     print("Borsa di studio rifiutata.")

# # ex.11
# free = 20
# status = True
# while status:
#     option = str(input("Inserisci opzione: "))
#     if option == "prenota":
#         if free > 0:
#             free -= 1
#         else:
#             print("Non ci sono posti disponibili.")
#     elif option == "libera":
#         if free < 20:
#             free += 1
#         else:
#             print("Tutti i posti sono già disponibili.")
#     elif option == "visualizza":
#         print(f"Posti liberi: {free}")
#     elif option == "esci":
#         status = False