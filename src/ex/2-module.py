# # ex. 1
# max = int(input("Inserisci numero massimo di posti: "))
# free = max
# while True:
#     option = str(input("Select option: "))
#     if option == "ingresso":
#         if free > 0:
#             free = free - 1
#         else:
#             print("Parking is full.")    
#     elif option == "uscita":
#         if free < max:
#             free = free + 1
#         else:
#             print("Parking's already empty.")
#     elif option == "stato":
#         print(f"Free parking slots: {free}, Occupied parking slots: {max-free}")
#     elif option == "quit":
#         break
#     else:
#         print("Error, select an option")

# # ex. 2
# ns = int(input("Cars from North-south: "))
# eo = int(input("Cars from East-ovest: "))
# soglia = int(input("Soglia auto: "))
# time = int(input("Time priority: "))
# if ns > soglia:
#     if eo > soglia:
#         timeNs = 50
#         timeEo = 50
#     else:
#         timeNs = time
#         timeEo = 100 - time
# elif eo > soglia:
#     timeNs = 100 - time
#     timeEo = time
# else:
#     tot = ns + eo
#     timeNs = ns/tot*100
#     timeEo = 100 - timeNs
# print(f"Time given to NS: {timeNs}, Time given to EO: {timeEo}")

# # ex. 3
# status = True
# while status:
#     nameCourse = str(input("Type course name: "))
#     max = 100
#     while True:
#         option = str(input("Select option: "))
#         if option.lower() == "add":
#             if max > 0:
#                 max -= 1
#             else:
#                 print("No available seat")
#         elif option.lower() == "remove":
#             if max < 100:
#                 max += 1
#             else: 
#                 print("Seats already available")
#         elif option.lower() == "show":
#             print(f"Free seats: {max}, Occupied seats: {100 - max}")
#         elif option.lower() == "delete":
#             break
#         elif option.lower() == "quit":
#             status = False
#             break

# # ex.4
# tutor = 10
# waiting = 0
# while waiting < 50:
#     student = (input("Name student: "))
#     if tutor > 0:
#         print("Tutor assigned")
#         tutor = tutor - 1
#     else:
#         waiting += 1
#         print(f"Added to the waiting list. {waiting}")
# print("Waiting list full.")

# # ex.5
# sum = 0
# i = 1
# n = int(input("Insert number: "))
# if n > 0:
#     while i <= n:
#         sum += i * i
#         i += 1
# else:
#     print("Error")
# print(f"The result is: {sum}")

# # ex.6
# x = int(input("Input number: "))
# if x > 0:
#     i = 1 
#     sum = 0
#     while i <= 10:
#         n = int(input(f"Insert 10 numbers {i}: "))
#         if n % 2 == 0:
#             if n > (x/2):
#                 sum = sum + n
#         elif n < x:
#             sum = sum + n
#         i = i + 1
#     print(sum)
# else:
#     print("Error")

# # ex. 7
# i = 1
# sum = 0
# while True:
#     option = input("Vuoi inserire voto?: ")
#     if option.lower() == "no":
#         print(f"La media dei voti è: {media}")
#         break
#     elif option.lower() == "si":
#         voto = int(input("Inserisci voto: "))
#         if voto > 0:
#             sum = sum + voto
#             media = sum / i
#             i = i+1 
#             #print(f"La media dei voti è: {media}")
#         else:
#             print("Errore")

# # ex. 8
# a = int(input("Type number: "))
# b = int(input("Type number: "))
# if a < b:
#     if a > 0 and b > 0:
#         if a % 1 == 0 and b % 1 == 0:
#             sum = 0
#             i = a
#             while i <= b:
#                 sum = sum + i
#                 i = i + 1
#             print(sum)
#         else:
#             print("A e B devono essere interi")
#     else:
#         print("A e B devono essere positivi")
# else:
#     print("A deve essere minore di B")

# # ex. 9
# while True:
#     n = int(input("Type divisore: "))
#     if n > 0 and n % 1 == 0:
#         cont = 0
#         i = 1
#         for i in range(10):
#             x = int(input("Type number: "))
#             if x % n == 0:
#                 cont += 1
#         print(f"I numeri divisibili sono: {cont}")
#     else:
#         print("Il numero deve essere intero positivo")

# # ex. 10
# age = int(input("Type your age: "))
# if age >= 18 and age <= 65:
#     print("Allowed to participate")
# elif age < 18:
#     print("Not allowed you're a minor.")
# else:
#     print("Not allowed over max age.")

# # ex. 11
# n = int(input("Type number: "))
# if n % 1 == 0:
#     if n % 2 == 0 and n > 10:
#         print("Number is valid")
#     else:
#         print("Number isn't valid")
# while True:
#     n = int(input("Type number: "))
#     if n % 1 == 0:
#         if n % 2 == 0 and n > 10:
#             print("Number is valid")
#             break
#         else:
#             print("Number isn't valid")

# # ex. 12
# n = int(input("Type number: "))
# i = 1
# for i in range(n):
#     x = int(input("Type x: "))
#     y = int(input("Type b: "))
#     if x > 0 and y > 0:
#         print(x*y)
#     elif x < 0 and y < 0:
#         print("Error")
#     else:
#         print(x-y)

# # ex. 13
# a = int(input("Input 1: "))
# b = int(input("Input 2: "))
# c = int(input("Input 3: "))

# if a < 0 or b < 0 or c < 0:
#     print("Hai messo un numero negativo")
# elif (a+b+c) % 2 == 0 and a % 2 == 0 and b % 5 == 0 and c % 7 == 0:
#     print("Regole rispettate")
# else: 
#     print("Regole non rispettate")

# ex. 14
# from random import randint
# die1 = 6
# die2 = 6
# total = 0
# points = 0

# status = True

# while status:
#     inp = str(input("Roll the dices?: "))
#     if inp.lower() == "yes":
#         roll1 = randint(1, die1)
#         roll2 = randint(1, die2)
#         print(f"Your rolls are {roll1} and {roll2}")
#         rollSum = roll1 + roll2
#         if (roll1 % 2 == 0 and roll2 % 2 == 0) and rollSum >= 8:
#             points = 100
#             print("You won the game!")
#             break
#         elif roll1 == 6 or roll2 == 6 or rollSum == 7:
#             points += 10
#             print(f"Your points are {points}")
#         else: 
#             points = 0
#             print("You lost!")
#             break
#     elif inp.lower() == "no":
#         break
# status = False
# print(f"Your score is {points}")
