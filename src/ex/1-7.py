i = 1
sum = 0
while True:
    option = input("Vuoi inserire voto?: ")
    if option.lower() == "no":
        print(f"La media dei voti è: {media}")
        break
    elif option.lower() == "si":
        voto = int(input("Inserisci voto: "))
        if voto > 0:
            sum = sum + voto
            media = sum / i
            i = i+1 
            #print(f"La media dei voti è: {media}")
        else:
            print("Errore")