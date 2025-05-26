from projectTypes import *

class Studente:
    _matricola: int 
    _nome: str
    _genere: str
    _telefono: set[Telefono]
    _email: set[Email]

    def matricola(self) -> int:
        return self._matricola
    
    def nome(self) -> str:
        return self._nome
    
    def genere(self) -> str:
        return self._genere
    
    def telefono(self) -> frozenset[Telefono]:
        return frozenset(self._telefono)