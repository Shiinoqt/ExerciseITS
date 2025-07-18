import random
from typing import Optional

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

class Mostro(Creatura):
    def __init__(self, nome: str, urlo_vittoria: Optional[str] = None, gemito_sconfitta: Optional[str] = None) -> None:
        super().__init__("Mostro")
        self.setNome(nome)
        self.setVittoria(urlo_vittoria)
        self.setSconfitta(gemito_sconfitta)
        self.setAssalto()

    def setAssalto(self) -> None:
        self._assalto = [random.randint(1, 100) for i in range(15)]

    def getAssalto(self) -> list[int]:
        return self._assalto

    def setVittoria(self, vittoria: str | None) -> None:
        if vittoria is not None:
            self._urlo_vittoria = vittoria
        else:
            self._urlo_vittoria = "GRAAAAHHHH"

    def getVittoria(self) -> str:
        return self._urlo_vittoria

    def setSconfitta(self, sconfitta: str | None) -> None:
        if sconfitta is not None:
            self._urlo_sconfitta = sconfitta
        else:
            self._urlo_sconfitta = "UUUUrrrghhh"
    
    def getSconfitta(self) -> str:
        return self._urlo_sconfitta

    def __str__(self) -> str:
        nome = self.getNome()
        newnome = ""
        for i in range(len(nome)):  
            if i % 2 == 1:
                newnome += nome[i].upper()
            else: 
                newnome += nome[i].lower()

        return f'Mostro: {newnome}'
    
def pariUguali(a: list[int], b: list[int]):
    c: list[int] = []

    if len(a) != len(b):
        raise ValueError("Le due liste devono avere la stessa lunghezza.")
    
    for i in range(len(a)):
        if (a[i] and b[i]) % 2 == 0:
            c.append(1)
        else:
            c.append(0)

    return c

def proclamaVincitore(c: Creatura):
    if not isinstance(c, Creatura):
        raise ValueError("Il vincitore deve essere una creatura valida.")
    
    if isinstance(c, Mostro):
        print('\nI Mostri hanno vinto!\n')
    else:
        print('\nGli Alieni hanno vinto!\n')
    
    height = 5
    # Metodo str
    creature_text = str(c)
    width = len(creature_text) + 10

    # Spazio disponibile togliendo la lunghezza di str e i due '*'
    available_space = width - 2 - len(creature_text)

    left_space = available_space // 2 
    right_space = available_space - left_space

    for i in range(height):
        if i == 0 or i == height - 1:  
            print('*' * width)
        elif i == 2: 
            print('*' + ' ' * left_space + creature_text + ' ' * right_space + '*')
        elif i == 1 or i == height - 2: 
            print('*' + ' ' * (width - 2) + '*')

def combattimento(a: Alieno, b: Mostro):
    if not isinstance(a, Alieno) or not isinstance(b, Mostro):
        print("Combattimento non valido: uno dei partecipanti non è della classe corretta.")
        return None
    
    a_munizioni = a.getMunizioni()
    b_assalto = b.getAssalto()

    c = pariUguali(a_munizioni, b_assalto)

    colpia = 0
    colpib = 0

    for i in range(len(c)):
        if c[i] == 1:
            colpia += 1
        else:
            colpib += 1

    if colpib >= 4:
        for i in range(0, 3):
            print(f'{b.getVittoria()}')

        proclamaVincitore(b)

    else:
        print(f'{b.getSconfitta()}')
        proclamaVincitore(a)


    

if __name__ == "__main__":
    alieno1 = Alieno()
    mostro1 = Mostro("gOrThOr")

    print(alieno1.__str__())
    print(alieno1.getMunizioni())
    print(f'\n{mostro1.__str__()}')
    print(mostro1.getAssalto())

    print(f'\nCombattimento\n')

    fight = combattimento(alieno1, mostro1)
