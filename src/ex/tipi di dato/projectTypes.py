from enum import *
from typing import Self, Any
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
    
class CAP(str):
    def __new__(cls, value: str) -> Self:
        if not re.match(r'\d{5}', value):
            raise ValueError("CAP non valido")
        return str.__new__(cls, value)

class CodiceFiscale(str):
    def __new__(cls, value: str) -> Self:
        if not re.match(r'[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]', value):
            raise ValueError("Codice Fiscale non valido")
        return str.__new__(cls, value)
    
class PartitaIva(str):
    def __new__(cls, value: str) -> Self:
        if not re.match(r'\d{11}', value):
            raise ValueError("Partita IVA non valida")
        return str.__new__(cls, value)

class Email(str):
    def __new__(cls, value: str) -> Self:
        if not re.match(r"\w+@\w+\.[a-z]{2,3}\.*[a-z]*", value):
            raise ValueError("Email non valida")
        return str.__new__(cls, value)
    
class Telefono(str):
    def __new__(cls, value: str) -> Self:
        if not re.match(r"\+?\d{1,3}?\d{1,4}?\d{4,10}", value):
            raise ValueError("Telefono non valido")
        return str.__new__(cls, value)
    
class StatoOrdine(StrEnum):
    preparazione = auto()
    inviato = auto()
    da_saldare = auto()
    saldato = auto()

class Aliquota(float):
    def __new__(cls, value: float) -> Self:
        if not (0 <= value <= 1):
            raise ValueError("Aliquota non valida")
        return float.__new__(cls, value)
    
class Imponibile(float):
    def __new__(cls, value: float) -> Self:
        if value < 0:
            raise ValueError("Imponibile non valido")
        return float.__new__(cls, value)

class RealGEZ(float):
    def __new__(cls, v: float|int|str|bool|Self) -> Self:
        n: float = float.__new__(cls, v)

        if n >= 0:
             return n
        
        raise ValueError("il valore N è negativo")

class Valuta(str):
    def __new__(cls, value: str) -> Self:
        if not re.match(r'^[A-Z]{3}$', value):
            raise ValueError("Valuta non valida")
        return str.__new__(cls, value)
    
class Denaro:
    def __init__(self, importo: float, valuta: Valuta) -> None:
        self._importo = importo
        self._valuta = valuta

    def __str__(self) -> str:
        return f"{self.importo():.2f} {self.valuta()}"
    
    def __eq__(self, other: Any):
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            return False
        return (self.importo(), self.valuta()) == (other.importo(), other.valuta())
    
    def importo(self):
        return self._importo
    
    def valuta(self):
        return self._valuta

    def __add__ (self, other: Self) -> Self:
        if self.valuta() != other.valuta():
            raise ValueError("Importi di valute diverse!")
        return Denaro(self.importo() + other.importo(), self.valuta())

class FloatDenaro(float):
    def __new__ (cls, importo: float, valuta: Valuta) -> Self:
        d = super().__new__(cls, importo)

        d._valuta = valuta
        return d

    def __str__(self) -> str:
        return f"{self.importo():.2f} {self.valuta()}"
    
    def __eq__(self, other: Any):
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            return False
        return (self.importo(), self.valuta()) == (other.importo(), other.valuta())
    
    def importo(self):
        return self.real
    
    def valuta(self):
        return self._valuta

    def __add__ (self, other: Self) -> Self:
        if self.valuta() != other.valuta():
            raise ValueError("Importi di valute diverse!")
        return Denaro(self.importo() + other.importo(), self.valuta())

class Citta:
    _nome: str
    _abitanti: int

    def __init__ (self, nome: str, abitanti: int) -> Self:
        self._nome = nome.strip().title()
        self._abitanti = abitanti

    def nome(self):
        return self._nome
    
    def abitanti(self):
        return self._abitanti
    
    def __eq__ (self, other):
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            return False
        return (self.nome(), self.abitanti()) == (other.nome(), other.abitanti())
    
    def __hash__(self):
        return hash((self._nome, self._abitanti))
    
class Nazione:
    _nome: str

    def __init__ (self, nome: str) -> Self:
        self._nome = nome.strip().title()

    def nome(self):
        return self._nome

    def __eq__ (self, other):
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            return False
        return self.nome() == other.nome()
    
    def __hash__(self):
        return hash(self.nome())

class IntGE1900(int):
    def __new__(cls, date: float|int|str|bool|Self):
        date: int = super().__new__(cls, date)

        if date < 1900:
            raise ValueError("")
        
        return date

class IntGEZ(int):
    def __new__(cls, value: float|int|str|bool|Self) -> Self:
        value: int = super().__new__(cls, value)

        if value <= 0:
            raise ValueError("")
        
        return value
    
class IntGZ(int):
    def __new__(cls, value: float|int|str|bool|Self) -> Self:
        value: int = super().__new__(cls, value)

        if value < 0:
            raise ValueError("")
        
        return value


# if __name__ == "__main__":
#     # Esempio di utilizzo
#     try:
#         cf = CodiceFiscale("RSSMRA85M01H501Z")
#         print(f"Codice Fiscale: {cf}")
#     except ValueError as e:
#         print(e)

#     # Esempio di utilizzo
#     myemails = {}

#     email1 = Email("email@yahoo.com")
#     email2 = Email("email@yahoo.com")

#     myemails[0] = email1
#     myemails[1] = email2
    
#     print(myemails[0] == myemails[1]) 
#     print(myemails[0] is myemails[1])

