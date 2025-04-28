from persona import Persona
from studente import Studente

fm: Persona = Persona("Francesco", "Mazzola", 25)

print(fm)

studente: Studente = Studente("Mario", "Rossi", 20, "121")

print(studente)

if isinstance(studente, Studente):
    print("Studente è un'istanza di Studente")

if isinstance(studente, Persona):
    print("Studente è un'istanza di Persona")

if isinstance(fm, Studente):
    print("fm è un'istanza di Studente")
else:
    print("fm non è un'istanza di Studente")

if isinstance(fm, Persona):
    print("fm è un'istanza di Persona")


if issubclass(Studente, Persona):
    print("Studente è una sottoclasse di Persona")


fm.speak()
studente.speak()