from projectTypes import *
import re

class Volo:
    _codice: str
    _durata_min: int

    def __init__(self, codice: str, durata_min: int) -> None:
        if durata_min <= 0:
            raise ValueError('Durata deve essere maggiore di 0')
        
        self._codice = codice
        self._durata_min = durata_min

    def codice(self) -> str:
        return self._codice
    
    def durata_min(self) -> int:
        return self._durata_min

    def __eq__(self, other):
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            return False
        return self.codice() == other.codice()
    
    def __hash__(self) -> int:
        return hash(self._codice)

class Compagnia:
    _nome: str
    _anno: int
    _voli: list[Volo]  

    def __init__(self, nome: str, anno: int) -> None:
        if anno <= 1900: 
            raise ValueError('Anno deve essere maggiore di 1900')
        
        self._nome = nome
        self._anno = anno
        self._voli = set[Volo] 

    def nome(self) -> str:
        return self._nome
    
    def anno(self) -> int:
        return self._anno
    
    def voli(self) -> frozenset[Volo]:
        return frozenset(self._voli)

    def aggiungiVolo(self, volo: 'Volo') -> None:
        self._voli.add(volo)
    
    def rimuoviVolo(self, volo: 'Volo') -> None:
        self._voli.discard(volo)  # discard non da errori se non lo trova
        
    def __eq__ (self, other):
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            return False
        return self.nome() == other.nome
    
    def __hash__(self) -> int:
        return hash(self._nome)


class Aeroporto:
    _codice: str
    _nome: str
    _citta: Citta

    def __init__(self, codice: str, nome: str) -> Self:
        if not re.match(r'^([A-Z]{3}|[A-Z0-9]{4})$', codice):
            raise ValueError('Codice aeroporto non valido')

        self._codice = codice
        self._nome = nome 
        self._citta = None

    def codice(self) -> str:
        return self._codice
        
    def nome(self) -> str:
        return self._nome
        
    def citta(self) -> Citta:
        return self._citta

    def setCitta(self, citta: Citta|None) -> None:
        self._citta = citta

    def __eq__ (self, other):
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            return False
        return self.codice() == other.codice()
    
    def __hash__(self):
        return hash(self._codice)

