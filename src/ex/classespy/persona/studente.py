from persona import Persona

class Studente(Persona):

    def __init__(self, nome:str, cognome:str, eta:int, matricola:str):

        super().__init__(nome, cognome, eta)

        self.setMatricola(matricola)

    def __str__(self) -> str:
        return f"{super().__str__()}, Matricola: {self.getMatricola()}" 

    def setMatricola(self, matricola:str) -> None:
        if matricola:
            self.matricola = matricola
        else:
            print("Matricola non valida")
    

    def getMatricola(self) -> str:
        return self.matricola