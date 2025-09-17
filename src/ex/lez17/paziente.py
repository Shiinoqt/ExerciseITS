from persona import Persona

class Paziente(Persona):
    def __init__ (self, id: str) -> None:
        super().__init__("", "")
        self.setId(id)

    def getId (self) -> str:
        return self.__id
    
    def setId (self, id: str) -> None:
        self.__id = id

    def patientInfo (self) -> str:
        return f"Paziente {self.get_first_name()} {self.get_last_name()}, ID: {self.getId()}."
    
