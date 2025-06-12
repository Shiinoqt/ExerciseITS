from impiegato import Impiegato
from progetto import Progetto
from datetime import date
from typing import Any

class coinvolto: # Associazione tra Impiegato e Progetto, classe che regola i link (classe "factory") 

    @staticmethod
    def add_link(cls, impiegato: Impiegato, progetto: Progetto, data_inizio: date) -> None:
        l = cls._link(impiegato, progetto, data_inizio)
        progetto._add_link_coinvolto(l)
        impiegato._add_link_coinvolto(l)


    class _link:
        _impiegato: 'Impiegato' # ovv. Immutable, noto alla nascita
        _progetto: 'Progetto' # ovv. Immutable, noto alla nascita
        _data_inizio: date # Immutable, noto alla nascita
        
        def __init__(self, impiegato: Impiegato, progetto: Progetto, data_inizio: date) -> None:
            self._impiegato = impiegato
            self._progetto = progetto
            self._data_inizio = data_inizio

        def impiegato(self) -> Impiegato:
            return self._impiegato
        
        def progetto(self) -> Progetto:
            return self._progetto
        
        def data_inizio(self) -> date:
            return self._data_inizio
        
        def __hash__(self) -> int:
            return hash((self._impiegato, self._progetto))
        
        def __eq__(self, other: Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            
            return (self.impiegato() is other.impiegato() and
                    self.progetto() is other.progetto())
        
        def __repr__(self) -> str:
            return (f"{self.impiegato()} è coinvolto in {self.progetto()} "
                    f"a partire dal {self.data_inizio()}")
