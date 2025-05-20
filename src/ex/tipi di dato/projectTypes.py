from enum import *


class Genere(StrEnum):
    uomo = auto()
    donna = auto()

class Indirizzo:
    def __init__ (self, via: str, civico: int):
        self._via = via
        self._civico = civico

    def via(self):
        return self._via
    
    def civico(self):
        return self._civico
    
    def __hash__(self):
        return hash((self._via, self._civico))
    
    def __eq__(self, other):
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            return False
        return (self.via(), self.civico()) == (other.via(), other.civico())
    
if __name__ == "__main__":
    i1 = Indirizzo("Via Roma", 1)
    i2 = Indirizzo("Via Roma", 1)
    i3 = Indirizzo("Via Milano", 2)
    
    print(i1 == i2)  # True
    print(i1 == i3)  # False
    print(i1 == None)  # False
    print(i1 == "Via Roma")  # False