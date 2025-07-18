from calcolacarico import calcolaCarico
from cariconullo import caricoNullo
from caricomax import caricoMax
from caricomin import caricoMin
from genera import genera
from printMAT import printMAT

matrice = genera(3)
printMAT(matrice)

print(f"\n")

print("Carico nullo:", caricoNullo(matrice))

print(f"\n")

carico_massimo = caricoMax(matrice)
print("Carico massimo:", carico_massimo)
print("Check carico massimo:", calcolaCarico(matrice, carico_massimo[0], carico_massimo[1]))

print(f"\n")

carico_minimo = caricoMin(matrice)
print("Carico minimo:", carico_minimo)
print("Check carico minimo:", calcolaCarico(matrice, carico_minimo[0], carico_minimo[1]))
