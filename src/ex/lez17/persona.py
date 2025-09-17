class Persona:
    __first_name: str
    __last_name: str
    __age: int

    def __init__(self, first_name, last_name) -> None:
        self.set_first_name(first_name)
        self.set_last_name(last_name)

        if self.__first_name is not None and self.__last_name is not None:
            self.__age = 0
        else:
            self.__age = None

    def get_first_name(self) -> str:
        return self.__first_name

    def set_first_name(self, first_name) -> None:
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            print("Il nome inserito non è una stringa!")
            self.__first_name = None

    def get_last_name(self) -> str:
        return self.__last_name
    
    def set_last_name(self, last_name) -> None:
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            print("Il cognome inserito non è una stringa!")
            self.__last_name = None

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age) -> None:
        if isinstance(age, int) and age >= 0:
            self.__age = age
        else:
            print("L'età deve essere un intero non negativo!")

    def greet(self) -> str:
        if self.get_first_name is None or self.get_last_name() is None or self.get_age() is None:
            raise Exception("Error: some attributes are not set")
        
        return f"Ciao, mi chiamo {self.get_first_name()} {self.get_last_name()} e ho {self.get_age()} anni."
