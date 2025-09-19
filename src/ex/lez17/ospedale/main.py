from dottore import Dottore
from paziente import Paziente
from fattura import Fattura
from persona import Persona

def main() -> None:
    # Crea due dottori
    dottore1 = Dottore("Mario", "Rossi", 45, "Cardiologia", 1000.0)
    dottore2 = Dottore("Luigi", "Bianchi", 50, "Neurologia", 1500.0)

    # Crea le liste di pazienti
    pazienti1 = [Paziente("Anna", "Verdi", 30, "P12345"),
                 Paziente("Luca", "Neri", 25, "P67890"),
                 Paziente("Sara", "Gialli", 40, "P54321")]
    
    pazienti2 = [Paziente("Marco", "Blu", 35, "P09876")]

    # I dottori si presentano
    print(dottore1.doctorGreet())
    print(dottore2.doctorGreet())

    # Crea le fatture
    fattura1 = Fattura(pazienti1, dottore1)
    fattura2 = Fattura(pazienti2, dottore2)

    # Stampa salario di ogni dottore
    print(f"Salario Dottore1: {fattura1.getSalary()} euro!")
    print(f"Salario Dottore2: {fattura2.getSalary()} euro!")

    # Rimuovi un paziente da dottore1 e aggiungilo a dottore2
    paziente_spostato = pazienti1.pop(0)
    pazienti2.append(paziente_spostato)

    # Aggiorna le fatture dopo lo spostamento
    fattura1 = Fattura(pazienti1, dottore1)
    fattura2 = Fattura(pazienti2, dottore2)

    # Stampa salario aggiornato
    print(f"Salario Dottore1: {fattura1.getSalary()} euro!")
    print(f"Salario Dottore2: {fattura2.getSalary()} euro!")

    # Calcola guadagno totale ospedale
    guadagno_totale = fattura1.getSalary() + fattura2.getSalary()
    print(f"In totale, l'ospedale ha incassato: {guadagno_totale} euro!")


if __name__ == "__main__":
    main()