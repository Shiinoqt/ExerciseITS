objects = []

for item in range(3):
    element = str(input("Type object to add: "))
    element = element.lower()
    objects.append(element)


match objects:
    case ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    case ["pane", "latte", "uova"]:
        print("Prodotti Alimentari")
    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")
    case ["telefono", "computer", "tablet"]:
        print("Dispositivi Elettronici")
    case _:
        print("Categoria Sconosciuta")
    