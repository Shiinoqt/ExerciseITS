from enum import *
from typing import *
import re

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
    
class PartitaIva(str):
    def __new__(cls, value: str):
        if not re.match(r'\d{11}', value):
            raise ValueError("Partita IVA non valida")
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
    
class StatoOrdine(StrEnum):
    preparazione = auto()
    inviato = auto()
    da_saldare = auto()
    saldato = auto()

class Aliquota(float):
    def __new__(cls, value: float):
        if not (0 <= value <= 1):
            raise ValueError("Aliquota non valida")
        return float.__new__(cls, value)
    
class Imponibile(float):
    def __new__(cls, value: float):
        if value < 0:
            raise ValueError("Imponibile non valido")
        return float.__new__(cls, value)

if __name__ == "__main__":
    # Esempio di utilizzo
    try:
        cf = CodiceFiscale("RSSMRA85M01H501Z")
        print(f"Codice Fiscale: {cf}")
    except ValueError as e:
        print(e)

    # Esempio di utilizzo
    myemails = {}

    email1 = Email("email@yahoo.com")
    email2 = Email("email@yahoo.com")

    myemails[0] = email1
    myemails[1] = email2
    
    print(myemails[0] == myemails[1]) 
    print(myemails[0] is myemails[1])




