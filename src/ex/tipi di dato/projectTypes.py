from enum import *
from typing import *
import re

class Genere(StrEnum):
    uomo = auto()
    donna = auto()

class StatoOrdine(StrEnum):
    preparazione = auto()
    inviato = auto()
    da_saldare = auto()
    saldato = auto()

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
    

class CodiceFiscale(str):
    def __new__(cls, value: str):
        if not re.match(r'[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]', value):
            raise ValueError("Codice Fiscale non valido")
        return str.__new__(cls, value)

class Email(str):
    def __new__(cls, value: str):
        if not re.match(r"\w+@\w+\.[a-z]{2,3}\.*[a-z]*", value):
            raise ValueError("Email non valida")
        return str.__new__(cls, value)
    
class Telefono(str):
    def __new__(cls, value: str):
        if not re.match(r"\+?\d{1,3}?\d{1,4}?\d{4,10}", value):
            raise ValueError("Telefono non valido")
        return str.__new__(cls, value)
    

if __name__ == "__main__":
    # Esempio per Genere
    print("Genere:", Genere.uomo, Genere.donna)

    # Esempio per StatoOrdine
    print("StatoOrdine:", StatoOrdine.preparazione, StatoOrdine.inviato, StatoOrdine.da_saldare, StatoOrdine.saldato)

    # Esempio per Indirizzo
    indirizzo = Indirizzo("Via Roma", 10)
    print("Indirizzo:", indirizzo.via(), indirizzo.civico())

    # Esempio per CodiceFiscale
    try:
        cf = CodiceFiscale("RSSMRA85T10A562S")
        print("CodiceFiscale:", cf)
    except ValueError as e:
        print(e)

    # Esempio per Email
    try:
        email = Email("esempio@email.com")
        print("Email:", email)
    except ValueError as e:
        print(e)

    # Esempio per Telefono
    try:
        telefono = Telefono("+390123456789")
        print("Telefono:", telefono)
    except ValueError as e:
        print(e)