animal = str(input("Digita il nome di un animale: "))


mammiferi = ["cane","gatto","elefante","leone"]
rettili = ["serpente","lucertola","tartaruga","coccodrillo"]
uccelli = ["aquila","pappagallo","gufo","falco"]
pesci = ["squalo","trota","salmone","carpa"]

match animal:
    case animal if animal in mammiferi:
        print(f"{animal.title()} appartiene ai mammiferi.")
    case animal if animal in rettili:
        print(f"{animal.title()} appartiene ai rettili.")
    case animal if animal in uccelli:
        print(f"{animal.title()} appartiene ai uccelli.")
    case animal if animal in pesci:
        print(f"{animal.title()} appartiene ai pesci.")
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animal}")
    