import random

class Creatura:
    def __init__(self, nome: str) -> None:
        self.setNome(nome)

    def setNome(self, nome: str) -> None:
        self.nome = "Creatura Generica"

        if isinstance(nome, str) and nome:
            self.nome = nome

    def getNome(self) -> str:
        return self.nome
    
    def __str__(self) -> str:
        return f"Creatura: {self.nome}"
    
class Alieno(Creatura):
    def __init__(self) -> None:
        super().__init__("Alieno")
        self.setNome("Robot-")
        self.setMatricola()
        self.setMunizioni()

    def getNome(self):
        return super().getNome()

    def setMatricola(self) -> None:
        self._matricola = random.randint(10000, 90000)

    def getMatricola(self) -> int:
        return self._matricola

    def setMunizioni(self) -> None:
        self._munizione = [i**2 for i in range(15)]

    def getMunizioni(self) -> list[int]:
        return self._munizione
    
    def __str__ (self) -> str:
        return f"Alieno: {self.getNome()+str(self.getMatricola())}"





if __name__ == "__main__":
    alieno1 = Alieno()
    print(alieno1.getMunizioni())
    print(alieno1.__str__())