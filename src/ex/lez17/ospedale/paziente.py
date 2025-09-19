from persona import Persona

class Paziente(Persona):
    def __init__(self, firstname, lastname, age, idCode) -> None:
        super().__init__(firstname, lastname)
        self.set_age(age)
        self.setIdCode(idCode)

    def setIdCode(self, idCode) -> None:
        self.__idCode = idCode

    def getIdCode(self) -> str:
        return self.__idCode

    def patientInfo(self) -> str:
        return f"Paziente: {self.get_first_name()} {self.get_last_name()}\nID: {self.__idCode}"