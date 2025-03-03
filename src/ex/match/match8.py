animal = str(input("Digita il nome di un animale: "))
habitat = str(input(f"Digita l'habitat in cui vive l'animale {animal}: "))


mammiferi = ["cane","gatto","cavallo","elefante","leone","balena","delfino"]
rettili = ["serpente","lucertola","tartaruga","coccodrillo"]
uccelli = ["aquila","pappagallo","gufo","falco","cigno","anatra","gallina","tacchino"]
pesci = ["squalo","trota","salmone","carpa"]

animalType : str

match animal:
    case animal if animal in mammiferi:
        print(f"{animal.title()} appartiene ai mammiferi.")
        animalType = "mammiferi"
    case animal if animal in rettili:
        print(f"{animal.title()} appartiene ai rettili.")
        animalType = "rettili"
    case animal if animal in uccelli:
        print(f"{animal.title()} appartiene ai uccelli.")
        animalType = "uccelli"
    case animal if animal in pesci:
        print(f"{animal.title()} appartiene ai pesci.")
        animalType = "pesci"
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animal}")
        animalType = "unknown"
    

myAnimal : dict[str] = {"animal": animal,"animalType": animalType,"habitat": habitat}



match myAnimal:
    case myAnimal if myAnimal["animalType"] == "mammiferi":
        if animal != ["delfino", "balena"] and habitat == "terra":
            print(f"L'animale {animal} è uno dei {animalType} che può vivere sulla terra")
        elif (animal == "delfino" or animalType == "balena") and habitat == "acqua":
            print(f"L'animale {animal} è uno dei {animalType} che può vivere sull'acqua")
        else:
            print(f"Non ho mai visto l'animale {animal} vivere nell'habitat {habitat}!")

    case myAnimal if myAnimal["animalType"] == "rettili":
        if habitat != "aria":
            print(f"L'animale {animal} è uno dei {animalType} che può vivere sulla {habitat}")
        else: 
            print(f"Non ho mai visto l'animale {animal} vivere nell'habitat {habitat}!")

    case myAnimal if myAnimal["animalType"] == "uccelli":
        if habitat != "acqua":
            print(f"L'animale {animal} è uno dei {animalType} che può vivere sulla {habitat}")
        else:
            print(f"Non ho mai visto l'animale {animal} vivere nell'habitat {habitat}!")
    case myAnimal if myAnimal["animalType"] == "pesci":
        if habitat != "terra" or habitat != "aria": 
            print(f"L'animale {animal} è uno dei {animalType} che può vivere sulla {habitat}")
        else:
            print(f"Non ho mai visto l'animale {animal} vivere nell'habitat {habitat}!")