from paziente import Paziente
from dottore import Dottore

class Fattura:
    def __init__(self, pazienti: list[Paziente], dottore: Dottore) -> None:
        if dottore.isAValidDoctor():
            self.dottore = dottore
            self.pazienti = pazienti
            self.fatture = len(pazienti)
            self.salary = 0
        else:
            self.pazienti = None
            self.dottore = None
            self.fatture = None
            self.salary = None
            print("Non è possibile creare la classe Fattura, il dottore non è valido!")

    def getSalary(self) -> float:
        if self.dottore and self.pazienti is not None:
            self.salary = self.fatture * self.dottore.getParcel()
            return self.salary
        return 0

    def getFatture(self) -> int:
        if self.pazienti is not None:
            self.fatture = len(self.pazienti)
            return self.fatture
        return 0
    
    def addPatient(self, paziente: Paziente) -> None:
        if self.pazienti is not None:
            self.pazienti.append(paziente)
            self.getFatture()
            self.getSalary()
            print(f"Il paziente {paziente.getIdCode()} è stato aggiunto alla fattura.")

    def removePatient(self, id_code: str) -> None:
        if self.pazienti is not None:
            dottore = self.dottore
            for paziente in self.pazienti:
                if paziente.getIdCode() == id_code:
                    self.pazienti.remove(paziente)
                    self.getFatture()
                    self.getSalary()
                    print(f"Alla lista del Dottor {dottore.get_last_name()} è stato rimosso il paziente con id {id_code}.")
                    return
            
            print(f"Il paziente con id {id_code} non è stato trovato nella fattura.")
