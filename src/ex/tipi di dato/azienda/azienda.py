import datetime
from projectTypes import *

class Progetto:
    nome: str
    budget: RealGEZ

class Impiegato:
    nome: str # non noto alla nascita
    cognome: str # non noto alla nascita
    nascita: datetime.date # non noto alla nascita
    stipendio: RealGEZ 
    progetti: set[Progetto] 