class Indirizzo:
    _via: str
    _civico: int

    def __init__ (self, via: str, civico: int) -> None:
        self._via = via
        self._civico = civico

    def via(self):
        return self._via
    
    def civico(self):
        return self._civico
    
    def __hash__(self) -> int:
        return hash((self._via, self._civico))
    
    def __eq__ (self, other: any) -> bool:
        if other is None or \
                not isinstance(other, type(self)) or \
                hash(self) != hash(other):
            return False
        return self._via == other._via and self._civico == other._civico
    

i1: Indirizzo = Indirizzo("Viale Cesare Pavese", 205)
i2: Indirizzo = Indirizzo("Viale Cesare Pavese", 205)

print(hash(i1) == hash(i2))

# d: dict[Indirizzo, int] = {}

# d[i1] = 9
# d[i2]

# print(d)
