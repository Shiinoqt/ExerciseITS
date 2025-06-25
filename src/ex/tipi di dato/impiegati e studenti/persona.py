from projectTypes import *
from datetime import datetime

class Persona:

    def __init__ (self, name: str, surname: str, cf: CodiceFiscale, nascita: datetime, maternità: IntGEZ, genere: Genere):
        self._setName(name)
        self._setSurname(surname)
        self._setCf(cf)
        self._nascita = nascita
        self._setMaternità(maternità)
        self._setGenere(genere)

    def setName(self, name: str) -> None:
        if not isinstance(name, str):
            raise ValueError("")
        
        self._name = name

    def setSurname(self, surname: str) -> None:
        if not isinstance(surname, str):
            raise ValueError()
        
        self._surname = surname
