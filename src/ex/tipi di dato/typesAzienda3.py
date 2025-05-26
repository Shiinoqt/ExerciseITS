from projectTypes import *
import datetime

class Impiegato:
    # Definizione dei campi dati
    _nome: str
    _cognome: str
    _nascita: datetime.date
    _stipendio: RealGEZ

    # Parte getter
    def nome(self) -> str:
        return self._nome
    
    def cognome(self) -> str:
        return self._cognome
    
    def nascita(self) -> datetime.date:
        return self._nascita
    
    def stipendio(self) -> RealGEZ:
        return self._stipendio

    # Parte setter
    def set_nome(self, nome: str) -> None:
        self._nome = nome
    
    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome

    def set_stipendio(self, stipendio: RealGEZ) -> None:
        self._stipendio = stipendio

    # Inizializzatore
    def __init__(self, nome: str, cognome: str, nascita: datetime.date, stipendio: RealGEZ) -> None:
        
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)

class Dipartimento:
    # Definizione dei campi dati
    _nome: str
    _telefono: set[Telefono]
    _indirizzo: Indirizzo

    # Parte getter
    def nome(self) -> str:
        return self._nome
    
    def telefono(self) -> frozenset[Telefono]:
        return frozenset(self._telefono)
    
    def indirizzo(self) -> Indirizzo:
        return self._indirizzo
    
    # Parte setter
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def add_telefono(self, telefono: Telefono) -> None:
        self._telefono.add(telefono)

    def remove_telefono(self, telefono: Telefono) -> None:
        self._telefono.remove(telefono)

    def set_indirizzo(self, indirizzo: Indirizzo|None) -> None:
        self._indirizzo = indirizzo

    # Inizializzatore
    def __init__(self, nome: str, telefono: Telefono, indirizzo: Indirizzo|None = None) -> None:
        self._telefono = set()
        
        self.set_nome(nome)
        self.add_telefono(telefono)
        self.set_indirizzo(indirizzo)

class Progetto:
    _nome: str
    _budget: RealGEZ

    def nome(self) -> str:
        return self._nome
    
    def budget(self) -> RealGEZ:
        return self._budget
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def set_budget(self, budget: RealGEZ) -> None:
        self._budget = budget

    def __init__(self, nome: str, budget: RealGEZ) -> None:
        self.set_nome(nome)
        self.set_budget(budget)