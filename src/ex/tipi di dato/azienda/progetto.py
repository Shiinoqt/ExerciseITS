from custom_types import RealGEZ
from coinvolto import coinvolto
from impiegato import Impiegato

class Progetto:

    _nome: str # noto alla nascita
    _budget: RealGEZ # noto alla nascita

    def __init__(self, nome: str, budget: RealGEZ) -> None:
        self._nome = nome
        self._budget = budget
        self._coinvolti: dict[Impiegato, coinvolto] = dict()

    def coinvolti(self) -> frozenset[coinvolto]:
        return frozenset(self._coinvolti.values())
    
    def coinvolto(self, impiegato: Impiegato) -> coinvolto:
        if impiegato not in self._coinvolti:
            raise KeyError(f"Impossibile trovare l'impiegato {impiegato.nome()} nel progetto {self.nome()}")
        return self._coinvolti[impiegato]

    def add_coinvolto(self, impiegato: Impiegato, data_inizio: str) -> None:
        if impiegato in self._coinvolti:
            raise KeyError(f"L'impiegato {impiegato.nome()} è già coinvolto nel progetto {self.nome()}")
        
        l: coinvolto = coinvolto(impiegato, self, data_inizio)
        self._coinvolti[impiegato] = l

    def remove_coinvolto(self, impiegato: Impiegato) -> None:
        if impiegato not in self._coinvolti:
            raise KeyError(f"L'impiegato {impiegato.nome()} non è coinvolto nel progetto {self.nome()}")
        del self._coinvolti[impiegato]

    def nome(self) -> str:
        return self._nome

    def budget(self) -> RealGEZ:
        return self._budget

    def get_nome(self) -> str:
        return self._nome

    def get_budget(self) -> RealGEZ:
        return self._budget

    def __str__(self) -> str:
        return f"Progetto '{self.nome()}' con budget: {self.budget()}€"

    def __repr__(self) -> str:
        return f"Progetto(nome={self.get_nome()}, budget={self.budget()})"