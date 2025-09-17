from persona import Persona

class Dottore(Persona):
    def __init__ (self, specialization: str, parcel: float) -> None:
        super().__init__("", "")
        self.setSpecialization(specialization)
        self.setParcel(parcel)

    def getSpecialization (self) -> str:
        return self.__specialization
    
    def setSpecialization (self, specialization: str) -> None:
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            print("The inserted specialization is not a string!")
            self.__specialization = None

    def getParcel (self) -> float:
        return self.__parcel
    
    def setParcel (self, parcel: float) -> None:
        if isinstance(parcel, float) and parcel >= 0:
            self.__parcel = parcel
        else:
            print("The inserted parcel is not valid!")
            self.__parcel = None

    def isAValidDoctor (self) -> bool:
        if self.get_age() > 30:
            print(f"Doctor {self.get_first_name()} {self.get_last_name()} is valid.")
            return True
        else:
            print(f"Doctor {self.get_first_name()} {self.get_last_name()} is not a valid.")
            return False
        
    def doctorGreet (self) -> str:
        return f"{self.greet()} Sono specializzato in: {self.getSpecialization()}."
    