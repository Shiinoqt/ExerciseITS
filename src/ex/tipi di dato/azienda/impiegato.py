from custom_types import RealGEZ
from progetto import Progetto
from datetime import date
# from coinvolto import coinvolto 
from coinvolto2 import coinvolto

class Impiegato:
    _nome: str # noto alla nascita
    _cognome: str # noto alla nascita
    _nascita: date # <<immutable>>, # noto alla nascita
    _stipendio: RealGEZ # # noto alla nascita
    _progetti: dict[Progetto, coinvolto._link] # da associazione [0..*], certamente non noto alla nascita

    def __init__(self, nome:str, cognome:str, nascita: date, stipendio: RealGEZ) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)
        self._progetti = dict() 

    def _add_link_coinvolto(self, l: coinvolto._link) -> None:
        if l.impiegato() is not self:
            raise ValueError(f"L'impiegato {self.nome()} non è lo stesso del link {l.impiegato().nome()}")
        if l.progetto() in self._progetti:
            raise KeyError(f"L'impiegato {self.nome()} è già coinvolto nel progetto {l.progetto().nome()}")
        self._progetti[l.progetto()] = l

    def _remove_link_coinvolto(self, l: coinvolto._link) -> None:
        if l.progetto() not in self._progetti:
            raise KeyError(f"L'impiegato {self.nome()} non è coinvolto nel progetto {l.progetto().nome()}")
        del self._progetti[l.progetto()]

    # def progetti(self) -> frozenset[coinvolto]:
    #     return frozenset(self._progetti.values())
    
    # def progetto(self, progetto: Progetto) -> coinvolto:
    #     if progetto not in self._progetti:
    #         raise KeyError(f"Impossibile trovare il progetto {progetto.nome()} per l'impiegato {self.nome()}")
    #     return self._progetti[progetto]
    
    # def add_progetto(self, progetto: Progetto, data_inizio: date) -> None:
    #     if progetto in self._progetti:
    #         raise KeyError(f"L'impiegato {self.nome()} è già coinvolto nel progetto {progetto.nome()}")
        
    #     l: coinvolto = coinvolto(self, progetto, data_inizio)
    #     self._progetti[progetto] = l

    # def remove_progetto(self, progetto: Progetto) -> None:
    #     if progetto not in self._progetti:
    #         raise KeyError(f"L'impiegato {self.nome()} non è coinvolto nel progetto {progetto.nome()}")
    #     del self._progetti[progetto]

    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def nascita(self) -> date:
        return self._nascita

    def stipendio(self) -> RealGEZ:
        return self._stipendio

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome

    def set_stipendio(self, stipendio: RealGEZ) -> None:
        self._stipendio = stipendio

    def __str__(self) -> str:
        return (f"{self.nome()} {self.cognome()}, "
                f"nascita: {self.nascita()}, "
                f"stipendio: {self.stipendio()}")
