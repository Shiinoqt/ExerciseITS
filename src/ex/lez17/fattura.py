from paziente import Paziente
from dottore import Dottore

class Fattura:
    pazienti: list[Paziente]
    dottore: Dottore
    fatture: int
    salary: int

    def __init__ (self, pazienti: list[Paziente], dottore: Dottore) -> None:
        if dottore.isAValidDoctor() == True:
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

    def getSalary (self) -> int:
        self.salary = self.fatture * self.dottore.getParcel()
        return self.salary
    
    def getFatture (self) -> int:
        self.fatture = len(self.pazienti)
        return self.fatture
    
    def addPatient (self, paziente: Paziente) -> None:
        self.pazienti.append(paziente)
        self.getFatture()
        self.getSalary()
        print(f"Il paziente {paziente.getId()} è stato aggiunto alla fattura.")
    
if __name__ == "__main__":
    dottore1 = Dottore("Cardiologo", 150.0)
    dottore1.set_first_name("Giovanni")
    dottore1.set_last_name("Verdi")
    dottore1.set_age(45)

    paziente1 = Paziente("P001")
    paziente1.set_first_name("Luca")
    paziente1.set_last_name("Bianchi")
    paziente1.set_age(30)

    paziente2 = Paziente("P002")
    paziente2.set_first_name("Anna")
    paziente2.set_last_name("Neri")
    paziente2.set_age(25)

    fattura1 = Fattura([paziente1, paziente2], dottore1)
    print(f"Il salario totale del dottore {dottore1.get_first_name()} {dottore1.get_last_name()} è: {fattura1.getSalary()} euro.")
    print(f"Numero di fatture emesse: {fattura1.getFatture()}.")

    paziente3 = Paziente("P003")
    paziente3.set_first_name("Marco")
    paziente3.set_last_name("Gialli")
    paziente3.set_age(40)

    fattura1.addPatient(paziente3)