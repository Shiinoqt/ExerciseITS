# ex. 1
maxi = int(input("Inserisci numero massimo di posti: "))
free = maxi

while True:
    option = str(input("Select option: "))
    if option == "ingresso":
        if free > 0:
            free = free - 1
        else:
            print("Parking is full.")    
    elif option == "uscita":
        if free < maxi:
            free = free + 1
        else:
            print("Parking's already empty.")
    elif option == "stato":
        print(f"Free parking slots: {free}, Occupied parking slots: {maxi-free}")
    elif option == "quit":
        break
    else:
        print("Error, select an option")